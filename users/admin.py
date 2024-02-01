from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'phone_number', 'is_staff')
    list_filter = ('role',)
    search_fields = ('full_name',)
