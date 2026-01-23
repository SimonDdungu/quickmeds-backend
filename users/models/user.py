from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from users.models import Role
import uuid



class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, username, email, password, role=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        
        if not role:
            role, _ = Role.objects.get_or_create(name="Staff")
            
        user = self.model(username, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):

        role, _ = Role.objects.get_or_create(name="Admin")
            
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        
        return self.create_user(username, email, password, role=role, **extra_fields)
            


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    def __str__(self):
        return self.username
