from django.urls import path, include
from rest_framework.router import DefaultRouter
from inventory.views import ManufacturerViewSet, BatchViewSet, MedicineViewSet, WholesalerViewSet

router = DefaultRouter()
router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'batch', BatchViewSet, basename='batch')
router.register(r'medicine', MedicineViewSet, basename='medicine')
router.register(r'wholesaler', WholesalerViewSet, basename='batch')

urlpatterns = [
    path('', include(router.urls)),
]