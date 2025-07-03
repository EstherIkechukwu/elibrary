
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


@admin.register(User)
class AuthorAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name",
                           "last_name", "email", "phone"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email', 'phone']
    list_display_links = ['email']
    list_per_page = 10


