from datetime import date
from inventory.models.batch import Batch
from rest_framework import serializers
from django.db import transaction
from sales.models import Sale
from sales.models.sale_item import SaleItem
from users.serializers import UserSerializer
from sales.serializers.sale_item import SaleItemSerializer



def get_valid_batches(medicine, quantity_needed):
    batches = Batch.objects.filter(medicine=medicine, quantity_remaining__gt=0, expiry_date__gt=date.today()).order_by('expiry_date') 

    choosen_batches = []
    remaining = quantity_needed

    for batch in batches:
        if remaining <= 0: # if we have all the tablets we want, we exit loop.
            break
        take = min(batch.quantity_remaining, remaining)  #take = min(6, 10) → batch A only has 6 tabs but we need 10 tabs, so we take the min (6) tablets from Batch A
        choosen_batches.append({'batch': batch, 'quantity': take}) # specify the batch we are taking the 6 tablets from
        remaining -= take  # After taking 6 tablets from Batch A, we need 4 tablets now, repeat with another batch.

    if remaining > 0:   # Lets say we wanted 20 tablets, but we only found 10 tablets, the remaining is 10 meaning, not enough stock.
        raise serializers.ValidationError(f"Not enough stock for {medicine.generic_name}. \nOnly {quantity_needed - remaining} units available."
        )
        
    return choosen_batches

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    saler_details = UserSerializer(source="sold_by", read_only=True)
    
    
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
            medicine = each_item["medicine"]
            quantity_sold = each_item["quantity"]
            # batch = each_item["batch"]
            
            valid_batches = get_valid_batches(medicine, quantity_sold)
            
            for each_valid_batch in valid_batches:
                batch = each_valid_batch["batch"]
                quantity = each_valid_batch['quantity']
                unit_price = batch.selling_price_per_unit
                sub_total = quantity * unit_price
                
                SaleItem.objects.create(
                    sale=sale,
                    medicine=medicine,
                    batch = batch,
                    quantity = quantity,
                    unit_price = unit_price,
                    sub_total = sub_total,
                    dosage_instruction = each_item.get("dosage_instruction", "")
                )
                
                batch.quantity_remaining -= quantity
                batch.save()
                
                total += sub_total
            
            
            
        sale.total_amount = total
        sale.save()
            
        return sale
    
    
    
    
    
    
    
    
    # if quantity_sold > batch.quantity_remaining:
            #     raise serializers.ValidationError("Not Enough Stock")
            
            # batch.quantity_remaining -= quantity_sold
            # batch.save()
            
            # each_item["sale"] = sale
            # SaleItemSerializer().create(each_item)
            
            # total += quantity_sold * each_item["unit_price"]