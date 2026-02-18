import logging
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from users.filters import UserFilterSet
from users.permissions import UserAuth
from users.models import User
from users.serializers import UserSerializer

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_class = [UserAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserFilterSet
    ordering_fields = ['created_at', 'updated_at', 'username', 'first_name', 'last_name']
    
    def handle_exception(self, exc):
        logger.error(f"User Error: {exc}")
        return super().handle_exception(exc)