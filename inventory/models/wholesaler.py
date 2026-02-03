from django.db import models
from inventory.constants.countries import COUNTRIES
from django.db.models import Q
import uuid

class Wholesaler(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    email = models.EmailField(blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country', 'address'],
                name='unique_Wholesaler',
            ),
            models.UniqueConstraint(
                fields=["contact"],
                condition= Q(contact__isnull=False) & ~Q(contact=""),
                name="unique_contact_if_present",
            ),
            models.UniqueConstraint(
                fields=["email"],
                condition=Q(email__isnull=False) & ~Q(email=""),
                name="unique_email_if_present",
            ),
        ]

    def __str__(self):
        return self.name
