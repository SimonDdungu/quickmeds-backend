from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from inventory.permissions import IsAdminOrTech
from inventory.models import Manufacturer
from inventory.serializers import ManufacturerSerializer
from inventory.filters import ManufacturerFilters

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    serializer_class = ManufacturerSerializer
    permission_class = [IsAdminOrTech]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ManufacturerFilters
    ordering_fields = ['name', 'country', 'created_at']