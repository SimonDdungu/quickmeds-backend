from django.db.models import Sum, Avg, Count
from django.utils import timezone
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from sales.models.sale import Sale
from sales.models.sale_item import SaleItem
from rest_framework.permissions import IsAuthenticated

class TodayDashboardKPIView(APIView):
    throttle_scope = 'default'
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)

        # Today's sales
        daily_sales = Sale.objects.filter(
            sold_at__date=today,
            status="Completed",
            sold_by=request.user
        )

        # Yesterday's completed sales
        yesterday_sales = Sale.objects.filter(
            sold_at__date=yesterday,
            status="Completed",
            sold_by=request.user
        )

        # Today's revenue
        daily_total_revenue = daily_sales.aggregate(total=Sum("total_amount"))["total"] or 0

        daily_transaction_count = daily_sales.count()

        daily_avg_transaction = daily_sales.aggregate(avg=Avg("total_amount"))["avg"] or 0

        daily_sold_units = SaleItem.objects.filter(
            sale__in=daily_sales
        ).aggregate(total=Sum("quantity"))["total"] or 0

        # Yesterday's totals
        yesterday_daily_revenue = yesterday_sales.aggregate(total=Sum("total_amount"))["total"] or 0

        yesterday_transaction_count = yesterday_sales.count()

        yesterday_avg_transaction = yesterday_sales.aggregate(avg=Avg("total_amount"))["avg"] or 0

        yesterday_sold_units = SaleItem.objects.filter(
            sale__in=yesterday_sales
        ).aggregate(total=Sum("quantity"))["total"] or 0

        
        def percentage_change(today_value, yesterday_value):
            if yesterday_value == 0:
                if today_value > 0:
                    return 100
                return 0
            change = ((today_value - yesterday_value) / yesterday_value) * 100
            return round(change, 2)

        data = {
            "daily_revenue": {
                "value": daily_total_revenue,
                "change_percentage": percentage_change(daily_total_revenue, yesterday_daily_revenue)
            },
            "average_transaction": {
                "value": round(daily_avg_transaction, 2),
                "change_percentage": percentage_change(daily_avg_transaction, yesterday_avg_transaction)
            },
            "number_of_transactions": {
                "value": daily_transaction_count,
                "change_percentage": percentage_change(daily_transaction_count, yesterday_transaction_count)
            },
            "sold_units": {
                "value": daily_sold_units,
                "change_percentage": percentage_change(daily_sold_units, yesterday_sold_units)
            }
        }

        return Response(data)