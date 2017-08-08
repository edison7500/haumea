from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserManager(BaseUserManager):
    pass


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True, db_index=True)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email