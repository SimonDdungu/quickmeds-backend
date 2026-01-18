from django.db import models
from users.models import User

class Sale(models.Model):
    sold_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sales')
    sold_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    receipt_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Sale {self.receipt_number}"
