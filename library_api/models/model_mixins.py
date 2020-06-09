from typing import Optional

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class LibraryBaseModel(models.Model):
    def as_queryset(self):
        # noinspection PyProtectedMember
        return self.__class__._default_manager.filter(pk=self.pk)

    class Meta:
        abstract = True


# noinspection PyAbstractClass
class GeoLocationMixin(LibraryBaseModel):
    lng = models.DecimalField(_("longitude"), max_digits=9, decimal_places=6, blank=True, null=True)

    lat = models.DecimalField(_("latitude"), max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        abstract = True


# noinspection PyAbstractClass
class AddressMixin(LibraryBaseModel):
    street_address = models.CharField(_("street address"), max_length=150, blank=True, null=True)
    street_address_2 = models.CharField(_("street address 2"), max_length=150, blank=True, null=True)
    postal_code = models.CharField(_("postal code"), max_length=30, blank=True, null=True)
    city = models.CharField(_("city"), max_length=150, blank=True, null=True)
    state = models.CharField(_("state"), max_length=150, blank=True, null=True)
    country = models.CharField(_("country"), max_length=150, blank=True, null=True)

    class Meta:
        abstract = True


# noinspection PyAbstractClass
class Timestampable(LibraryBaseModel):
    """
    Adds implementation of the created_at and updated_at datetimes. Uses the timezone specified in the settings.
    Save method is overridden to make sure the updated_at also is in the correct timezone.
    """

    created_at = models.DateTimeField(_("created at"), default=timezone.now, editable=False)

    updated_at = models.DateTimeField(_("updated at"), default=timezone.now)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updated_at = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)
