from inventory.models.manufacturer import Manufacturer
from inventory.serializers.manufacturer import ManufacturerSerializer
from rest_framework import serializers
from inventory.models import Medicine, DOSAGE_FORMS, STRENGTH_UNITS

class MedicineSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all(), write_only=True)
    manufacturer_detail = ManufacturerSerializer(source="manufacturer", read_only=True)
    dosage_form = serializers.ChoiceField(choices=DOSAGE_FORMS, required=False, allow_null=True, default=None)
    strength_unit = serializers.ChoiceField(choices=STRENGTH_UNITS, required=False, allow_null=True, default=None)
    strength = serializers.DecimalField(max_digits=6, decimal_places=2,
        error_messages={
            'max_digits': 'Strength limit: 9,999.99',
            'max_decimal_places': 'Strength limit: 9,999.99',
            'max_whole_digits': 'Strength limit: 9,999.99',
            }
    )
    
    class Meta:
        model = Medicine
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'current_price']
        
        
    def validate_strength(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Medicine Strength can not be negative")
        
        if value >=10000:
            raise serializers.ValidationError("Medicine Strength can not be exceed 9,999.99")
        
        return value
    
    
    
class MedicineSummarySerializer(serializers.ModelSerializer):
    current_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    manufacturer_detail = ManufacturerSerializer(source="manufacturer", read_only=True)
    class Meta:
        model = Medicine
        exclude = ['created_at', 'updated_at', 'manufacturer', ]