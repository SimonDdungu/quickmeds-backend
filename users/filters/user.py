from django_filters import rest_framework as filters
from users.models import User
from django.db.models import Q

class UserFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_fullname_search')
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    username = filters.CharFilter(field_name='username', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    phone_number = filters.CharFilter(field_name='phone_number', lookup_expr='icontains')
    
    
    class Meta:
        model = User
        fields = ['gender']
        
    def filter_fullname_search(self, queryset, name, value):
        return queryset.filter(
        Q(sold_by__first_name__icontains=value) |
        Q(sold_by__last_name__icontains=value) |
        Q(sold_by__username__icontains=value)
    )