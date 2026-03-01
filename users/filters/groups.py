from django_filters import rest_framework as filters
from django.contrib.auth.models import Group

class GroupsFilterSet(filters.FilterSet):
    role = filters.CharFilter(field_name='name', lookup_expr='icontains')
    
    class Meta:
        model = Group
        fields = []
