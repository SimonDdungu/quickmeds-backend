from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from sales.filters import SaleFilterSet
from sales.permissions import IsAdminOrTech
from sales.models import Sale
from sales.serializers import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    #permission_class = [IsAdminOrTech]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = SaleFilterSet
    ordering_fields = ['sold_at', 'updated_at', 'total_amount']
    