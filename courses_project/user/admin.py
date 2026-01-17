from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'full_name',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_editable = (
        'full_name',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'role',
    )
    ordering = ('id',)
