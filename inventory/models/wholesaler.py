from django.db import models
from inventory.constants.countries import COUNTRIES
import uuid

class Wholesaler(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    email = models.EmailField(unique=True, blank=True, null=True)
    contact = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country', 'address'],
                name='unique_Wholesaler',
            )
        ]

    def __str__(self):
        return self.name
