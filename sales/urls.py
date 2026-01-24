from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales.views import SaleViewSet, SaleItemViewSet

router = DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'saleitems', SaleItemViewSet, basename='sale_items')

urlpatterns = [
    path('', include(router.urls))
]

