from django_filters import rest_framework as filters
from django.db.models import Q
from inventory.models import Batch

class BatchFilters(filters.FilterSet):
    search = filters.CharFilter(method='filter_medicine_search')
    wholesaler = filters.CharFilter(field_name='wholesaler__name', lookup_expr='icontains')
    
    selling_price_minimum = filters.NumberFilter(field_name='selling_price_per_unit', lookup_expr='gte')
    selling_price_maximum = filters.NumberFilter(field_name='selling_price_per_unit', lookup_expr='lte')
    
    purchase_price_minimum = filters.NumberFilter(field_name='purchase_price', lookup_expr='gte')
    purchase_price_maximum= filters.NumberFilter(field_name='purchase_price', lookup_expr='lte')
    
    quantity_received_min = filters.NumberFilter(field_name='quantity_received', lookup_expr='gte')
    quantity_received_max = filters.NumberFilter(field_name='quantity_received', lookup_expr='lte')
    
    quantity_remaining_min = filters.NumberFilter(field_name='quantity_remaining', lookup_expr='gte')
    quantity_remaining_max = filters.NumberFilter(field_name='quantity_remaining', lookup_expr='lte')
    
    expiry_date_from = filters.DateFilter(field_name='expiry_date', lookup_expr='gte')
    expiry_date_to   = filters.DateFilter(field_name='expiry_date', lookup_expr='lte')
    
    
    
    class Meta:
        model = Batch
        fields = ['batch_number', 'purchase_price', 'selling_price_per_unit', 'quantity_received', 'quantity_remaining', 'expiry_date']
        
    def filter_medicine_search(self, queryset, name, value):
        return queryset.filter(
            Q(medicine__name__icontains=value) |
            Q(medicine__generic_name__icontains=value)
        )