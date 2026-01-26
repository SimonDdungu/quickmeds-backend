from rest_framework.views import APIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from rest_framework import status
from users.serializers import PasswordResetRequestSerializer
from users.models import User

class PasswordResetRequestView(APIView):
    permission_classes = []
    
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data["email"].lower()
        
        try:
            token_generator = PasswordResetTokenGenerator()
            
            user = User.objects.get(email__iexact=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            
            reset_link = f"https://quickmeds/reset-password/?uid={uid}&token={token}"
            
        
        except User.DoesNotExist:
            pass
        
        return Response({"Response": "If Email exists, Reset Password link has been sent."}, status=status.HTTP_200_OK)
        
        
        