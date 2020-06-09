import uuid
from datetime import timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _

from library_api import settings
from library_api.models.model_mixins import Timestampable, AddressMixin
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, Timestampable):
    USERNAME_FIELD = 'email'

    objects = UserManager()

    first_name = models.CharField(
        _('first name'),
        max_length=255)

    last_name = models.CharField(
        _('last name'),
        max_length=255)

    phone = models.CharField(_("phone mobile"), max_length=255, blank=True, default="")

    email = models.EmailField(
        _('email address'), unique=True)

    date_joined = models.DateTimeField(
        _('date joined'),
        blank=True, null=True
    )

    # SETTINGS

    is_staff = models.BooleanField(
        _('is staff'),
        default=False
    )

    is_active = models.BooleanField(
        _('is active'),
        default=False
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name} – {self.email}"

    # pylint: disable=arguments-differ
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
