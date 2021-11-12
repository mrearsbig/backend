from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, fullname, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
            password = password,
            fullname = fullname,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, password, fullname, **extra_fields):
        return self._create_user(email, username, password, fullname, **extra_fields)

    def create_superuser(self, email, username, password, fullname, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, username, password, fullname, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()
    username = models.CharField(max_length = 50, unique = True)
    fullname = models.CharField(max_length = 150)
    cellphone = models.CharField(max_length = 15, blank = True, null = True)
    city = models.CharField(max_length = 70, blank = True, null = True)
    address = models.CharField(max_length = 150, blank = True, null = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'fullname']