from rest_framework import serializers
from inventory.models import Wholesaler

class WholesalerSerializers(serializers.ModelSerializers):
    class meta:
        model = Wholesaler
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    