from rest_framework.views import APIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from users.serializers import PasswordResetConfirm
from users.models import User

class PasswordResetConfirmView(APIView):
    permission_class = []
    
    def post(self, request):
        serializer = PasswordResetConfirm(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        uid = serializer.validated_data["uid"]
        token = serializer.validated_data["token"]
        new_password = serializer.validated_data["new_password"]
        
        
        try:
            user_id = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=user_id)
        except Exception:
            raise ValidationError("Invalid Reset Link.")
        
        token_generator = PasswordResetTokenGenerator()
        
        if token_generator.check_token(user, token):
            raise ValidationError("Invalid or Expired Token")
        
        user.set_password(new_password)
        user.save()
        
        return Response({"detail": "Password reset successful"}, status=status.HTTP_200_OK)

            