from django.db import models
from .medicine import Medicine
from .wholesaler import Wholesaler
import uuid

class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches')
    wholesaler = models.ForeignKey(Wholesaler, on_delete=models.PROTECT, related_name='batches')
    batch_number = models.CharField(max_length=50)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_received = models.IntegerField()
    quantity_remaining = models.IntegerField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine.name} - {self.batch_number}"
