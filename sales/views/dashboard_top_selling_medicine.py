from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from sales.models.sale_item import SaleItem
from rest_framework.permissions import IsAuthenticated


class TopSellingMedicinesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        today = timezone.now().date()
        start_date = today.replace(day=1)  # first day of current month

        top_medicines = (
            SaleItem.objects.filter(
                sale__sold_at__date__gte=start_date,
                sale__sold_at__date__lte=today,
                sale__status="Completed",
                sale__sold_by=request.user
            )
            .values("medicine__id", "medicine__generic_name")
            .annotate(total_sold=Sum("quantity"))
            .order_by("-total_sold")[:5]
        )

        data = [{ "medicine_id": item["medicine__id"], "medicine__generic_name": item["medicine__generic_name"], "total_sold": item["total_sold"] } for item in top_medicines]

        return Response({
            "start_date": start_date,
            "end_date": today,
            "data": data
        })