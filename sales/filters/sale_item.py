from django_filters import rest_framework as filters
from sales.models import SaleItem

class SaleItemFilterSet(filters.FilterSet):
    medicine = filters.CharFilter(field_name='medicine_name', lookup_expr='icontains')
    batch = filters.CharFilter(field_name='batch_number', lookup_expr='icontains')
    
    quantity_min = filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity_max = filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    
    unit_price_min = filters.NumberFilter(field_name='unit_price', lookup_expr='gte')
    unit_price_max = filters.NumberFilter(field_name='unit_price', lookup_expr='lte')

    
    class Meta:
        model = SaleItem
        fields = ['quantity', 'unit_price', 'sale__id', 'created_at', 'updated_at']