from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

class CookieTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data["refresh"]
        access = response.data["access"]
        
        # Set access token in HttpOnly cookie
        response.set_cookie(
            key="access_token",
            value=access,
            httponly=True,
            secure=False,  # True in production
            samesite="Lax",
            max_age=15 * 60,  # 5 minutes (match access lifetime)
            path="/"
        )


        # Set refresh token in HttpOnly cookie
        response.set_cookie(
            key="refresh_token",
            value=refresh,
            httponly=True,
            secure=False,  # True in production with HTTPS
            samesite="Lax",
            max_age=30*24*60*60,  # 30 days
            path="/"
        )

        # # Remove refresh from response body so JS cannot access it
        # response.data.pop("refresh", None)
        
        # Remove tokens from response body
        response.data = {"detail": "Login successful"}
        return response