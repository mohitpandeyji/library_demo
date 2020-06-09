from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.models import (
    User
)

admin.site.unregister(Group)


# noinspection PyClassHasNoInit
# pylint: disable=bad-continuation
class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = [
        "id",
        "email",
        "is_superuser",
    ]
    list_filter = ["is_superuser"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    fieldsets = (
        (None, {"fields": ["password"]}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_superuser")},),
        (
            "Important dates",
            {"fields": ("updated_at", "date_joined",)},
        ),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2",), },),
    )
    search_fields = ("email", "id")
    ordering = ["-id"]
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
