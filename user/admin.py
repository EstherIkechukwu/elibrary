from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author

# Register your models here.

@admin.register(Author)
class AuthorAdmin(UserAdmin):
    pass

