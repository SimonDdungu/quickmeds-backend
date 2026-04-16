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
        request = self.context.get("request")
        user = request.user if request else None

        password = validated_data.pop('password')
        role = validated_data.pop('role', 'Cashier')
        
        if role == "Admin":
            allowed_groups = ["Admin"]
            if not user or not user.groups.filter(name__in=allowed_groups).exists():
                raise serializers.ValidationError(
                    {"detail": f"You are not allowed to assign {role} role"}
                )
        
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
        request = self.context.get("request")
        user = request.user if request else None
       
        role = validated_data.pop('role', None)
        
        if role == "Admin":
            allowed_groups = ["Admin"]
            if not user or not user.groups.filter(name__in=allowed_groups).exists():
                raise serializers.ValidationError(
                    {"detail": f"You are not allowed to assign {role} role"}
                )
                
        # Admin can not downgrade there own role.        
        if instance == user and role != "Admin":
            raise serializers.ValidationError({"detail": "Admins cannot remove their own admin role"})

        if role:
            group = Group.objects.get(name=role)
            instance.groups.clear()
            instance.groups.add(group)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['profile_image']:
            data['profile_image'] = 'https://kmmrgijtqahiilujqbck.supabase.co/storage/v1/object/public/QuickMeds/profile/profile_placeholder.png'
        return data