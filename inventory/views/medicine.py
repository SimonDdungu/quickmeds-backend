from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from inventory.models import Medicine
from inventory.serializers import MedicineSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    #permission_class = [IsAuthenticated]
    
    
    