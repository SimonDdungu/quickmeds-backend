from rest_framework import serializers
from datetime import date
from inventory.models import Batch

class BatchSerializer(serializers.ModelSerializer):
    class meta:
        model = Batch
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def validate_quantity_received(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity received can not be less than 1!")
        return value
    
    def validate_quantity_remaining(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity remaining can not be less than 0!")
        return value
    
    def validate_expiry_date(self, value):
        if value <= date.today():
            raise serializers.ValidationError("Medicine Batch is already expired!")
        return value
    
    def validate_purchase_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Purchase price cannot be negative.")
        return value

    def validate_selling_price_per_unit(self, value):
        if value < 0:
            raise serializers.ValidationError("Selling price cannot be negative.")
        return value
    
    def validate(self, data):
        quanityRemaining = data.get('quantity_remaining')
        quanityReceived = data.get('quantity_received')
        
        if quanityRemaining is not None and quanityRemaining > quanityReceived:
            raise serializers.ValidationError("Quantity remaining can not exceed Quantity received!")
        return data
    
    def create(self, validated_data):
        validated_data["quanity_remaining"] = validated_data["quanity_received"]
        return super().create(validated_data)
    
    
