from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response

class CookieTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        refresh = request.COOKIES.get("refresh_token")
        
        if not refresh:
            return Response({"detail": "No refresh token"}, status=401)

        serializer = self.get_serializer(data={"refresh": refresh})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        response = Response({"detail": "Token refreshed"})
        
        response.set_cookie(
            key="access_token",
            value=data["access"],
            httponly=True,
            secure=True,
            samesite="None",
            max_age=15 * 60,
            path="/"
        )

        
        if "refresh" in data:
            response.set_cookie(
                key="refresh_token",
                value=data["refresh"],
                httponly=True,
                secure=True,
                samesite="None",
                max_age=30*24*60*60,
                path="/"
            )
            
        return response