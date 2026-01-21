from rest_framework import serializers
from sales.models import SaleItem
from inventory.serializers import MedicineSerializers

class SaleItemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializers(read_only=True)
    medicine_id = serializers.UUIDField(write_only=True)
    
    class meta:
        model = SaleItem
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        
    def create(self, validated_data):
        medicine_id = validated_data.pop("medicine_id")
        validated_data["medicine"] = SaleItem.objects.get(id=medicine_id)
        return super().create(validated_data)
    

