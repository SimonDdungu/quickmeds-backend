from django.db import models
from .manufacturer import Manufacturer
import uuid

DOSAGE_FORMS = [
    ('tablet', 'Tablet'),
    ('capsule', 'Capsule'),
    ('syrup', 'Syrup'),
    ('injection', 'Injection'),
]

STRENGTH_UNITS = [
    ('mg', 'mg'),
    ('g', 'g'),
    ('µg', 'µg'),
    ('IU', 'IU'),
    ('ml', 'ml'),
    ('mg/mL', 'mg/mL'),
    ('µg/mL', 'µg/mL'),
    ('IU/mL', 'IU/mL')
]

class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)     #Brand Name E.g called Panadol
    generic_name = models.CharField(max_length=100, blank=True)     #Like Flavor or Type, Different Panadols include Panadol Extra, Paracetamol, Cold and Flu
    dosage_form = models.CharField(max_length=20, choices=DOSAGE_FORMS, blank=True)         #Tablet
    strength = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)       #500
    strength_unit = models.CharField(max_length=10, choices=STRENGTH_UNITS, blank=True, null=True)      #mg
    description = models.TextField(blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='medicines')
    image = models.ImageField(upload_to='medicine_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'generic_name', 'dosage_form', 'strength', 'strength_unit', 'manufacturer'],
                name='unique_medicine'
            )
        ]
        

    def __str__(self):
        return self.name
