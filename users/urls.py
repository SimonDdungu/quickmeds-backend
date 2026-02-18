from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PasswordResetConfirmView, PasswordResetRequestView, RoleList


router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/roles/', RoleList.as_view(), name='roles'),
    path('api/auth/password-reset/', PasswordResetRequestView.as_view()),
    path('api/auth/password-reset-confirm/', PasswordResetConfirmView.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

