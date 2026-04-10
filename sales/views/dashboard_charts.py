from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from sales.models.sale import Sale
from rest_framework.views import APIView
from rest_framework.response import Response

class SalesTrendView(APIView):
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