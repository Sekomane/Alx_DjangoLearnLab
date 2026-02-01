from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields shown in the admin list view
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
    )

    # Fields shown when viewing/editing a user
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "date_of_birth",
                    "profile_photo",
                )
            },
        ),
    )

    # Fields shown when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "date_of_birth",
                    "profile_photo",
                )
            },
        ),
    )
