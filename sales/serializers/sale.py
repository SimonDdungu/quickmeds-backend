from rest_framework import serializers
from django.db import transaction
from sales.models import Sale
from users.serializers import UserSerializer
from sales.serializers.sale_item import SaleItemSerializer

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    soldby = UserSerializer(read_only=True)
    
    
    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ["id", "sold_by", "sold_at", "total_amount", 'updated_at']
     
    @transaction.atomic 
    def create(self, validated_data):
        all_items = validated_data.pop("items")
        sale = Sale.objects.create(**validated_data)
        
        total = 0
        
        for each_item in all_items:
            
            batch = each_item["batch"]
            quantity_sold = each_item["quantity"]
            
            if quantity_sold > batch.quantity_remaining:
                raise serializers.ValidationError("Not Enough Stock")
            
            batch.quantity_remaining -= quantity_sold
            batch.save()
            
            each_item["sale"] = sale
            SaleItemSerializer().create(each_item)
            
            total += quantity_sold * each_item["unit_price"]
            
        sale.total_amount = total
            
        return sale.save()