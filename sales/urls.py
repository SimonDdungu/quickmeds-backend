from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales.views import SaleViewSet, SaleItemViewSet, TodayDashboardKPIView, SalesTrendView, TopSellingMedicinesView, MonthlySalesTrendView, WeeklyItemsSoldView

router = DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'saleitems', SaleItemViewSet, basename='sale_items')

urlpatterns = [
    path('', include(router.urls)),
    path("dashboard/kpi/me/", TodayDashboardKPIView.as_view()),
    path("dashboard/charts/me/weekly_sales/", SalesTrendView.as_view()),
    path("dashboard/charts/me/monthly_sales/", MonthlySalesTrendView.as_view()),
    path("dashboard/charts/me/weekly_items/", WeeklyItemsSoldView.as_view()),
    path("dashboard/charts/me/top_selling_medicine/", TopSellingMedicinesView.as_view()),
]

