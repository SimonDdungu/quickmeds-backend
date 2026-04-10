from django.db import models
from users.models import User
from sales.constants.status import STATUS
import uuid

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sold_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sales')
    sold_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS, default="Completed", db_index=True)
    
    
    class Meta:
        ordering = ['-sold_at']
        
    def __str__(self):
        return f"Reciept Number: {self.id}"
