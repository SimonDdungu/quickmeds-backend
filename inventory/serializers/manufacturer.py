from rest_framework import serializers
from inventory.models import Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
    class meta:
        model = Manufacturer
        fields = '__all__'
        
        