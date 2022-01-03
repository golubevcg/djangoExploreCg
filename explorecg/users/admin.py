from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import ECGUser


@admin.register(ECGUser)
class AuthorAdmin(UserAdmin):
    list_display = "username", "id", "first_name", "last_name", "email"
