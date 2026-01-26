from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from users.models import Role
from users.constants import GENDER
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
            #role, _ = Role.objects.get_or_create(name="Cashier")
            role, _ = Group.objects.get_or_create(name="Cashier")
            
        
        email = email.lower()
        extra_fields.setdefault("is_staff", True)
        user = self.model(username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.groups.add(role)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):

        #role, _ = Role.objects.get_or_create(name="Admin")
        admin_group, _ = Group.objects.get_or_create(name="Admin")
            
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        
        return self.create_user(username, email, password, role=admin_group, **extra_fields)
            


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    #role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username
