from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import update_session_auth_hash

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        old_password = request.data.get("old_password")
        new_password = request.data.get("password")

        if not old_password or not new_password:
            return Response({"detail": "old_password and new_password are required"}, status=status.HTTP_400_BAD_REQUEST )

        if not user.check_password(old_password):
            return Response({"detail": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST )
        
  
        user.set_password(new_password)
        user.save()

        # keep user logged in after changing passwords
        update_session_auth_hash(request, user)

        return Response({"detail": "Password changed successfully"})