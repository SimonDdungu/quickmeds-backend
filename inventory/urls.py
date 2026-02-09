from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import ManufacturerViewSet, BatchViewSet, MedicineViewSet, WholesalerViewSet
from inventory.views.country import countries_list
from inventory.views.medicine_choices import dosage_form_list, strength_unit_list

router = DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register(r'batches', BatchViewSet, basename='batch')
router.register(r'medicine', MedicineViewSet, basename='medicine')
router.register(r'wholesalers', WholesalerViewSet, basename='wholesaler')

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', countries_list, name='countries-list'),
    path('dosage_form/', dosage_form_list, name='dosage-form-list'),
    path('strength_unit/', strength_unit_list, name='strength-unit-list'),
]