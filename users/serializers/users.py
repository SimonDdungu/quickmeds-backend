from rest_framework import serializers
from django.contrib.auth.models import Group
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')

    password = serializers.CharField(write_only=True, required=False)
    role = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'groups', 'email', 'phone_number', 'gender', 'profile_image', 'role', 'password', 'is_active', 'is_superuser', 'groups', 'created_at', 'updated_at',]
        read_only_fields = ['id', 'groups', 'created_at', 'updated_at']
        
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
            
            
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        role = validated_data.pop('role', None)
        if role:
            group = Group.objects.get(name=role)
            instance.groups.clear()
            instance.groups.add(group)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance