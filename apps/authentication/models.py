from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from apps.home.models import * 
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError("The given username must be set")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)



class NewUser(AbstractBaseUser, PermissionsMixin):
    # basic information

    email = models.EmailField(('email address'))
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)# Permissions
    institute = models.ForeignKey(Institution ,on_delete=models.CASCADE,null=True,blank=True)
    supervisor = models.ForeignKey(Supervisor ,on_delete=models.CASCADE,verbose_name="supervisor",null=True,blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    confirm_password = models.CharField(max_length=100)
    is_supervisor = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='images')




    def clean(self):
        if self.password  !=  self.password1:
            raise ValidationError("password are incorrect")

    
    objects = UserManager()

    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username

