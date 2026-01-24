from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group

class RoleList(APIView):
    def get(self, request):
        roles = Group.objects.values_list('name', flat=True)
        return Response({"roles": list(roles)})