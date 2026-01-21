from django.db import models
from .medicine import Medicine
from .wholesaler import Wholesaler
from datetime import date
import uuid

class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches')
    wholesaler = models.ForeignKey(Wholesaler, on_delete=models.PROTECT, related_name='batches')    
    batch_number = models.CharField(max_length=50)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_received = models.PositiveIntegerField()           # 24 tablets (Box)
    quantity_remaining = models.PositiveIntegerField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['medicine', 'wholesaler', 'batch_number'],
                name='unique_batches_per_medicine'
            )
        ]

    def __str__(self):
        return f"{self.medicine.name} - {self.batch_number} expires {self.expiry_date}"
    
    def is_expired(self):
        return date.today() > self.expiry_date
    
    def is_expiring_soon(self, expires_in_days=30):
        days_left = (self.expiry_date - date.today()).days
        if 0 <= days_left <= expires_in_days:      #if not yet expired (0) but within expiry days (30)... E.G: 0 days left (It has already expired) <= 5 days left <= 30 days to expire - True is expiring soon
            return days_left
        else:
            return None
        