from rest_framework import serializers
from inventory.models import Wholesaler

class WholesalerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wholesaler
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    