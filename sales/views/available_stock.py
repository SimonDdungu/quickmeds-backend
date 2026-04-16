from django.db.models import Sum
from datetime import date
from django.shortcuts import get_object_or_404
from inventory.models.batch import Batch
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from inventory.models.medicine import Medicine

class AvailableStockView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, medicine_id):
        medicine = get_object_or_404(Medicine, id=medicine_id)
        
        total = Batch.objects.filter(
            medicine=medicine,
            quantity_remaining__gt=0,
            expiry_date__gt=date.today()
        ).aggregate(total_quantity=Sum('quantity_remaining'))['total_quantity']

        return Response({"available_stock": total})