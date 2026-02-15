import logging
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from inventory.permissions.roles import IsAdminOrTech
from inventory.models import Manufacturer
from inventory.serializers import ManufacturerSerializer
from inventory.filters import ManufacturerFilters

logger = logging.getLogger(__name__)

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    #permission_class = [IsAdminOrTech]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ManufacturerFilters
    ordering_fields = ['name', 'country', 'created_at', 'updated_at']
    
    
    def handle_exception(self, exc):
        logger.error(f"Manufacturer Error: {exc}")
        return super().handle_exception(exc)