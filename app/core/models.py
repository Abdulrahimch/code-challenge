from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
                                       BaseUserManager

from django.core.validators import RegexValidator, MaxValueValidator, \
                                   MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    TC_regex = RegexValidator(regex=r'^[1-9]\d{10}$', message="TC number must have 11 digits, should not start with Zero")
    TC = models.CharField(validators=[TC_regex], max_length=11, unique=True)
    gsm_regex = RegexValidator(regex=r'^\+?9?\d{9,15}$', message="Phone number must be entered in the format: '+90 5xx xxx xxxx'. Up to 15 digits allowed.")
    gsm = models.CharField(validators=[gsm_regex], max_length=15)
