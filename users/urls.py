from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, GroupViewSet, CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView, ChangePasswordView


router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path("auth/login/", CookieTokenObtainPairView.as_view(), name="get_tokens"),
    path("auth/logout/", LogoutView.as_view(), name="logout"), 
    path("auth/token/refresh/", CookieTokenRefreshView.as_view(), name="refresh_tokens"),
    path("auth/password/new/", ChangePasswordView.as_view(), name="change_password"),    
]