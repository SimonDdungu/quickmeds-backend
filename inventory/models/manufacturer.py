from django.db import models
import uuid

class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True)
    contact_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country'],
                name='unique_manufacturer'
            )
        ]

    def __str__(self):
        return self.name
