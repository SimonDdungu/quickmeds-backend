from django.db import models
from .sale import Sale
from inventory.models import Medicine, Batch
import uuid

class SaleItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    dosage_instruction = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity} x {self.medicine.generic_name}"
