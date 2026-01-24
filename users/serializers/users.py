from rest_framework import serializers
from django.contrib.auth.models import Group
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.pop('role', 'cashier')
        
        try:
            group = Group.objects.get(name=role)
        except Group.DoesNotExist:
            raise serializers.ValidationError("Role does not exist")
        
        
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        user.groups.add(group)
        return user
            