from django_filters import rest_framework as filters
from sales.models import SaleItem

class SaleItemFilterSet(filters.FilterSet):
    medicine = filters.CharFilter(field_name='medicine__name', lookup_expr='icontains')
    batch = filters.CharFilter(field_name='batch__batch_number', lookup_expr='icontains')
    
    quantity_min = filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity_max = filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    
    unit_price_min = filters.NumberFilter(field_name='batch__selling_price_per_unit', lookup_expr='gte')
    unit_price_max = filters.NumberFilter(field_name='batch__selling_price_per_unit', lookup_expr='lte')

    
    class Meta:
        model = SaleItem
        fields = ['quantity', 'batch__selling_price_per_unit', 'sale__id', 'created_at', 'updated_at']