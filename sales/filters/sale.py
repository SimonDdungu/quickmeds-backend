from django_filters import rest_framework as filters
from sales.models import Sale
from django.db.models import Q

class SaleFilterSet(filters.FilterSet):
    sold_by = filters.CharFilter(method='filter_fullname_search')
    
    total_min = filters.NumberFilter(field_name='total_amount', lookup_expr='gte')
    total_max = filters.NumberFilter(field_name='total_amount', lookup_expr='lte')
    
    sold_from = filters.DateFilter(field_name='sold_at', lookup_expr='gte')
    sold_to = filters.DateFilter(field_name='sold_at', lookup_expr='lte')
    
    
    class Meta:
        model = Sale
        fields = ['id', 'total_amount', 'sold_at', 'status']
        
    def filter_fullname_search(self, queryset, name, value):
        return queryset.filter(
        Q(sold_by__first_name__icontains=value) |
        Q(sold_by__last_name__icontains=value) |
        Q(sold_by__username__icontains=value)
    )