from django_filters import rest_framework as filters
from inventory.models import Manufacturer

class ManufacturerFilters(filters.ModelFilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    country = filters.CharFilter(field_name='country', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    contact = filters.CharFilter(field_name='contact', lookup_expr='icontains')
    
    class Meta:
        model = Manufacturer
        
        
    