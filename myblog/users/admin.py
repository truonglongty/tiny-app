from django.contrib import admin
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