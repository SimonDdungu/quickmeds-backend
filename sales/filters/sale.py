from django_filters import rest_framework as filters
from sales.models import Sale

class SaleFilterSet(filters.FilterSet):
    sold_by = filters.CharFilter(field_name='sold_by__username', lookup_expr='icontains')
    
    total_max = filters.NumberFilter(field_name='total_amount', lookup_expr='gte')
    total_min = filters.NumberFilter(field_name='total_amount', lookup_expr='lte')
    
    sold_from = filters.DateFilter(field_name='sold_at', lookup_expr='gte')
    sold_to = filters.DateFilter(field_name='sold_at', lookup_expr='lte')
    
    
    class Meta:
        model = Sale
        fields = ['total_amount', 'sold_at']