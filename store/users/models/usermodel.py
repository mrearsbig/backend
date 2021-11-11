from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.fields import BooleanField

class UserManager(BaseUserManager):
    def create_user(self, email, username, password, fullname):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
            fullname = fullname
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, fullname):
        user = self.create_user(
            email = email,
            username = username,
            password = password,
            fullname = fullname
        )
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField()
    username = models.CharField(max_length = 50, unique = True)
    password = models.CharField(max_length = 256)
    fullname = models.CharField(max_length = 150)
    cellphone = models.CharField(max_length = 15, blank = True, null = True)
    city = models.CharField(max_length = 70, blank = True, null = True)
    address = models.CharField(max_length = 150, blank = True, null = True)
    is_active = BooleanField(default = True)
    is_admin = BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username', 'password', 'fullname']