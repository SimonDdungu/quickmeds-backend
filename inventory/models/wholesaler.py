from django.db import models

class Wholesaler(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    branch = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
