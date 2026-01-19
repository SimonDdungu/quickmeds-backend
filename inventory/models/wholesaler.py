from django.db import models
import uuid

class Wholesaler(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country', 'address'],
                name='unique_Wholesaler',
            )
        ]

    def __str__(self):
        return self.name
