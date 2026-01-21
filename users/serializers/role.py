from rest_framework import serializers
from users.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class meta:
        model = Role
        field = '__all__'