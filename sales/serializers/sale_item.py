from rest_framework import serializers
from sales.models import SaleItem
from inventory.models import Medicine, Batch
from inventory.serializers import MedicineSerializer, BatchSerializer

class SaleItemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)
    batch = BatchSerializer(read_only=True)
    medicine_id = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all(), write_only=True, source='medicine')
    batch_id = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all(), write_only=True, source='batch')
    
    class Meta:
        model = SaleItem
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        