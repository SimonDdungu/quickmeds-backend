from rest_framework import serializers
from inventory.models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
        
    def validate_strength(self, value):
        if value < 0:
            raise serializers.ValidationError("Medicine Strength can not be negative")
        return value