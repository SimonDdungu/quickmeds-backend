from django_filters import rest_framework as filters
from inventory.models import Wholesaler

class WholesalerFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    country = filters.CharFilter(field_name='country', lookup_expr='icontains')
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    contact = filters.CharFilter(field_name='contact', lookup_expr='icontains')
    
    class Meta:
        model = Wholesaler