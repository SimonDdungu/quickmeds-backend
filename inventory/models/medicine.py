from django.db import models
from .manufacturer import Manufacturer

DOSAGE_FORMS = [
    ('tablet', 'Tablet'),
    ('capsule', 'Capsule'),
    ('syrup', 'Syrup'),
    ('injection', 'Injection'),
]

STRENGTH_UNITS = [
    ('mg', 'mg'),
    ('g', 'g'),
    ('ml', 'ml'),
    ('IU', 'IU'),
]

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100, blank=True)
    dosage_form = models.CharField(max_length=20, choices=DOSAGE_FORMS, blank=True)
    strength = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    strength_unit = models.CharField(max_length=10, choices=STRENGTH_UNITS, blank=True, null=True)
    description = models.TextField(blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='medicines')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
