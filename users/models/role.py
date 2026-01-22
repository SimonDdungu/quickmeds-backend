from django.db import models

class Role(models.Model):
    slug = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    