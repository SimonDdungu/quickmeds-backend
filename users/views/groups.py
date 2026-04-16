# views.py
from django.contrib.auth.models import Group
from rest_framework import viewsets, filters
from users.serializers import GroupSerializer
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from users.filters import GroupsFilterSet
from users.permissions.permissions import RolePermission

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [RolePermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GroupsFilterSet
    
    def get_queryset(self):
        user = self.request.user

        qs = Group.objects.all()

        # hide Admin options
        allowed_groups = ["Admin"]
        if not user.groups.filter(name__in=allowed_groups).exists():
            qs = qs.exclude(name__in=allowed_groups)

        return qs