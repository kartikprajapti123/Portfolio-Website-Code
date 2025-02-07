from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group,Permission
from uuid import uuid4
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
# Create your models here.
class User(AbstractUser):
    user_uuid=models.UUIDField(default=uuid4,null=True,blank=True)
    username = models.CharField(max_length=20,null=True)
    profile_picture=models.FileField(upload_to='user_profile_image',default="user_profile_image/user-profile.png")
    country=models.CharField(max_length=100,default="India",null=True,blank=True)
    phone=models.CharField(max_length=100,default="1231231231",null=True,blank=True)
    
    email = models.EmailField(unique=True)
    password=models.CharField(null=True)
    otp=models.CharField(max_length=6,null=True)
    is_verified=models.BooleanField(default=False)
    deleted=models.IntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoid conflict with default User.groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoid conflict with default User.user_permissions
        blank=True,
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email