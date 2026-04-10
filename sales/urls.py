from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales.views import SaleViewSet, SaleItemViewSet, TodayRevenueView, TodayAllRevenueView, TodayAllSoldUnitsView, TodaySoldUnitsView
from sales.views.dashboard_kpi import TodayDashboardKPIView

router = DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'saleitems', SaleItemViewSet, basename='sale_items')

urlpatterns = [
    path('', include(router.urls)),
    path("dashboard/kpi/me/", TodayDashboardKPIView.as_view()),
]

