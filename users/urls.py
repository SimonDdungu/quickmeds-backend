from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PasswordResetConfirmView, PasswordResetRequestView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('password-reset/', PasswordResetRequestView.as_view()),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view()),
]

