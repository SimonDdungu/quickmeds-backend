from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from inventory.filters import BatchFilters
from inventory.permissions.roles import IsAdminOrTech
from inventory.models import Batch
from inventory.serializers import BatchSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    #permission_class = [IsAdminOrTech]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BatchFilters
    ordering_fields = ['expiry_date', 'created_at', 'updated_at', 'selling_price_per_unit', 'purchase_price', 'quantity_received', 'quantity_remaining']
    
    
    