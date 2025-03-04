from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib import messages

class UserAdmin(BaseUserAdmin):
    actions = ['block_user', 'unblock_user', 'reset_password']

    def block_user(self, request, queryset):
        queryset.update(is_active=False)
        messages.success(request, "Selected users have been blocked.")

    block_user.short_description = "Block selected users"

    def unblock_user(self, request, queryset):
        queryset.update(is_active=True)
        messages.success(request, "Selected users have been unblocked.")

    unblock_user.short_description = "Unblock selected users"

    def reset_password(self, request, queryset):
        for user in queryset:
            form = AdminPasswordChangeForm(user, {'password1': 'new_password', 'password2': 'new_password'})
            if form.is_valid():
                form.save()
        messages.success(request, "Passwords for selected users have been reset to 'new_password'.")

    reset_password.short_description = "Reset password for selected users"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
=======
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
>>>>>>> main
