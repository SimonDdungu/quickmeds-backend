from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from inventory.models import Wholesaler
from inventory.serializers import WholesalerSerializers

class WholesalerViewSet(viewsets.ModelViewSet):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializers
    #permission_class = [IsAuthenticated]
    
    
    