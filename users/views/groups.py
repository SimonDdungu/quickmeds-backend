# views.py
from django.contrib.auth.models import Group
from rest_framework import viewsets, filters
from users.serializers import GroupSerializer
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from users.filters import GroupsFilterSet

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GroupsFilterSet
    