from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from django.contrib import messages

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_blocked', 'is_staff', 'is_active')
    list_filter = ('is_blocked', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_blocked', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    actions = ['block_users', 'unblock_users']

    def block_users(self, request, queryset):
        queryset.update(is_blocked=True)
        messages.success(request, "Selected users have been blocked.")

    def unblock_users(self, request, queryset):
        queryset.update(is_blocked=False)
        messages.success(request, "Selected users have been unblocked.")

    block_users.short_description = "Block selected users"
    unblock_users.short_description = "Unblock selected users"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)