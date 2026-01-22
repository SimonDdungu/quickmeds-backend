from django_filters import rest_framework as filters
from inventory.models import Batch

class BatchFilters(filters.FilterSet):
    medicine = filters.CharFilter(field_name='medicine__name', lookup_expr='icontains')
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