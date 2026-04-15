import logging
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from inventory.permissions.permissions import InventoryPermission
from inventory.models import Medicine
from inventory.serializers import MedicineSerializer, MedicineSummarySerializer
from inventory.filters import MedicineFilterSet

logger = logging.getLogger(__name__)

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [InventoryPermission]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MedicineFilterSet
    ordering_fields = ['created_at', 'updated_at', 'name', 'generic_name', 'dosage_form', 'strength', 'strength_unit', 'manufacturer__name']
    
   
    
    def handle_exception(self, exc):
        logger.error(f"Medicine Error: {exc}")
        return super().handle_exception(exc)
  
  
class MedicineSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSummarySerializer
    permission_classes = [InventoryPermission]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MedicineFilterSet
    ordering_fields = ['created_at', 'updated_at', 'name', 'generic_name', 'dosage_form', 'strength', 'strength_unit', 'manufacturer__name']
    
   
    
    def handle_exception(self, exc):
        logger.error(f"Medicine Error: {exc}")
        return super().handle_exception(exc)
