import logging
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from sales.filters import SaleFilterSet
from sales.permissions import IsAdminOrTech
from sales.models import Sale
from sales.serializers import SaleSerializer
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class SaleViewSet(viewsets.ModelViewSet):
    throttle_scope = 'default'
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    #permission_class = [IsAdminOrTech]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = SaleFilterSet
    ordering_fields = ['sold_at', 'updated_at', 'total_amount']
    
    def perform_create(self, serializer):
        serializer.save(sold_by=self.request.user)
        
    #Block PUT requests, Allow Only PATCH requests. 
    def update(self, request, *args, **kwargs):
        if kwargs.get('partial', False):
            return super().update(request, *args, **kwargs)
        
        return Response({"error": "Sales cannot be changed."}, status=status.HTTP_403_FORBIDDEN)
        
    
    
    #Block DELETE requests
    def destroy(self, request, *args, **kwargs):
        return Response({"error": "Sales cannot be deleted."}, status=status.HTTP_403_FORBIDDEN)
    
    def handle_exception(self, exc):
        logger.error(f"Sale Error: {exc}")
        return super().handle_exception(exc)
    