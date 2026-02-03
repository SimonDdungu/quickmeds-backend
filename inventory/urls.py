from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import ManufacturerViewSet, BatchViewSet, MedicineViewSet, WholesalerViewSet
from inventory.views.country import countries_list

router = DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register(r'batch', BatchViewSet, basename='batch')
router.register(r'medicine', MedicineViewSet, basename='medicine')
router.register(r'wholesalers', WholesalerViewSet, basename='wholesaler')

urlpatterns = [
    path('', include(router.urls)),
    path('countries/', countries_list, name='countries-list'),
]