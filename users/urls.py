from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PasswordResetConfirmView, PasswordResetRequestView, GroupViewSet, CookieTokenObtainPairView, CookieTokenRefreshView


router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/password-reset/', PasswordResetRequestView.as_view()),
    path('auth/password-reset-confirm/', PasswordResetConfirmView.as_view()),
    path("auth/login/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"), 
    # path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]

# path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/auth/roles/', RoleList.as_view(), name='roles'),
    # path("auth/token/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("auth/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"), 