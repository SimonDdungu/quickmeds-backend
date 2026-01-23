from django_filters import rest_framework as filters
from inventory.models import Medicine

class MedicineFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    generic_name = filters.CharFilter(field_name='generic_name', lookup_expr='icontains')
    dosage_form = filters.CharFilter(field_name='dosage_form', lookup_expr='icontains')
    strength_min = filters.NumberFilter(field_name='strength', lookup_expr='gte')
    strength_max = filters.NumberFilter(field_name='strength', lookup_expr='lte')
    strength_unit = filters.CharFilter(field_name='strength_unit', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    manufacturer = filters.CharFilter(field_name='manufacturer__name', lookup_expr='icontains')
    
    class Meta:
        model = Medicine
        fields = ['strength']