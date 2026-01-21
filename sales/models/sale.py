from django.db import models
from users.models import User
import uuid

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sold_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sales')
    sold_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Sale {self.receipt_number}"
