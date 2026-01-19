from django.contrib import admin
from .models import Medicine, Batch, Manufacturer, Wholesaler

admin.site.register(Medicine)
admin.site.register(Batch)
admin.site.register(Manufacturer)
admin.site.register(Wholesaler)
