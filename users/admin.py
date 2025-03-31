from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ['username', 'email']
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)