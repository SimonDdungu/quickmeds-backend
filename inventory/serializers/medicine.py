from inventory.models.manufacturer import Manufacturer
from inventory.serializers.manufacturer import ManufacturerSerializer
from rest_framework import serializers
from inventory.models import Medicine, DOSAGE_FORMS, STRENGTH_UNITS

class MedicineSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all(), write_only=True)
    manufacturer_detail = ManufacturerSerializer(source="manufacturer", read_only=True)
    dosage_form = serializers.ChoiceField(choices=DOSAGE_FORMS, required=False, allow_null=True, default=None)
    strength_unit = serializers.ChoiceField(choices=STRENGTH_UNITS, required=False, allow_null=True, default=None)
    
    class Meta:
        model = Medicine
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
        
    def validate_strength(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Medicine Strength can not be negative")
        return value
    
    
    
class MedicineSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        exclude = ['created_at', 'updated_at']