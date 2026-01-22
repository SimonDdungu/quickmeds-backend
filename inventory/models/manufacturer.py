from django.db import models
import uuid

class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=True)
    contact = models.CharField(max_length=15, unique=True, blank=True)
    address = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name', 'country']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country', 'email', 'address'],
                name='unique_manufacturer_email'
            ),
            models.UniqueConstraint(
                fields=['name', 'country', 'contact', 'address'],
                name='unique_manufacturer_contact'
            )
        ]

    def __str__(self):
        return self.name
