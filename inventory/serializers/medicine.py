from rest_framework import serializers
from inventory.models import Medicine

class MedicineSerializers(serializers.ModelSerializers):
    class Meta:
        model = Medicine
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        