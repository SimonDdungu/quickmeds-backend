from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from sales.models.sale import Sale
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import ExtractMonth, ExtractYear
from sales.models.sale_item import SaleItem
from rest_framework.permissions import IsAuthenticated

class SalesTrendView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        today = timezone.now().date()
        start_date = today - timedelta(days=6)

        sales = (
            Sale.objects.filter(
                sold_at__date__gte=start_date,
                sold_at__date__lte=today,
                status="Completed",
                sold_by=request.user
            )
            .values("sold_at__date")
            .annotate(total=Sum("total_amount"))
            .order_by("sold_at__date")
        )

        # To fill in for missing days
        sales_map = {item["sold_at__date"]: item["total"] for item in sales}

        data = []
        for i in range(7):
            day = start_date + timedelta(days=i)
            data.append({
                "date": day,
                "total": sales_map.get(day, 0)
            })

        return Response({
            "start_date": start_date,
            "end_date": today,
            "data": data
        })
        




class MonthlySalesTrendView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        today = timezone.now().date()

        # First day of current month
        current_month_start = today.replace(day=1)

        # Go back 5 months
        start_date = current_month_start - relativedelta(months=5)

        sales = (
            Sale.objects.filter(
                sold_at__date__gte=start_date,
                sold_at__date__lte=today,
                status="Completed",
                sold_by=request.user
            )
            .annotate(
                month=ExtractMonth("sold_at"),
                year=ExtractYear("sold_at")
            )
            .values("year", "month")
            .annotate(total=Sum("total_amount"))
            .order_by("year", "month")
        )

 
        sales_map = {(item["year"], item["month"]): item["total"] for item in sales }

        # Build 6-month timeline
        data = []
        current = start_date # 6th month, not current

        for _ in range(6):
            year = current.year
            month = current.month

            data.append({
                "year": year,
                "month": month,
                "total": sales_map.get((year, month), 0)
            })

            # move month forward safely
            current += relativedelta(months=1)

        return Response({
            "start_date": start_date,
            "end_date": today,
            "data": data
        })
        
        
        
        
class WeeklyItemsSoldView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        today = timezone.now().date()

        # Today = April 11 2026            Monday = 0, SUnday = 6
        #start_of_week = April 11 - 3 days to get Monday. "3 days" is which day of the week are we?
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        items = (
            SaleItem.objects.filter(
                sale__sold_at__date__gte=start_of_week,
                sale__sold_at__date__lte=end_of_week,
                sale__status="Completed",
                sale__sold_by=request.user
            )
            .values("sale__sold_at__date")
            .annotate(total=Sum("quantity"))
            .order_by("sale__sold_at__date")
        )
        
        items_map = { item["sale__sold_at__date"]: item["total"]  for item in items }
        
        data = []
        for i in range(7):
            day = start_of_week + timedelta(days=i)

            data.append({
                "date": day,
                "total": items_map.get(day, 0)
            })

        return Response({
            "start_date": start_of_week,
            "end_date": end_of_week,
            "data": data
        })