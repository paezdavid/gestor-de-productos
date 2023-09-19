from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    # Crear un usuario
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # Crear un superuser
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('user_is_approved', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    user_is_approved = models.BooleanField(default=False)

    objects = CustomUserManager()