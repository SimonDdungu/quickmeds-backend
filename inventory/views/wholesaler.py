from rest_framework import viewsets, filters
from inventory.permissions.roles import IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from inventory.filters import WholesalerFilterSet
from inventory.models import Wholesaler
from inventory.serializers import WholesalerSerializers

class WholesalerViewSet(viewsets.ModelViewSet):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializers
    #permission_class = [IsAdmin]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = WholesalerFilterSet
    ordering_fields = ['name', 'country', 'created_at', 'updated_at']
    
    