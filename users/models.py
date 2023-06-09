import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=15, default='')
    surname = models.CharField(max_length=15, default='')
    phone_number = models.IntegerField(default=0000000000)
    skills = models.CharField(max_length=50, default='')
    experience = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    dark_mode = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.email
