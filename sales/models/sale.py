from django.db import models
from users.models import User
import uuid

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sold_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sales')
    sold_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-sold_at']
        
    def __str__(self):
        return f"Sale: {self.receipt_number}"
