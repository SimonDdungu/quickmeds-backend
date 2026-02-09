from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from inventory.permissions.roles import IsAdminOrTech
from inventory.models import Medicine
from inventory.serializers import MedicineSerializer
from inventory.filters import MedicineFilterSet
from rest_framework.response import Response
from rest_framework import status

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    #permission_class = [IsAdminOrTech]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MedicineFilterSet
    ordering_fields = ['created_at', 'updated_at', 'name', 'generic_name', 'dosage_form', 'strength', 'strength_unit', 'manufacturer__name']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
    
    