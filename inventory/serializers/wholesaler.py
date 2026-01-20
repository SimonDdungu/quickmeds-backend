from rest_framework import serializers
from inventory.models import Wholesaler

class WholesalerSerializers(serializers.ModelSerializers):
    class meta:
        model = Wholesaler
        field = '__all__'
        
    