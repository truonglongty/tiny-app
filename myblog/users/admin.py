from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

def block_users(modeladmin, request, queryset):
    for user in queryset:
        user.profile.is_blocked = True
        user.profile.save()
block_users.short_description = "Block selected users"

def unblock_users(modeladmin, request, queryset):
    for user in queryset:
        user.profile.is_blocked = False
        user.profile.save()
unblock_users.short_description = "Unblock selected users"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'is_staff', 'is_blocked')
    actions = [block_users, unblock_users]

    def is_blocked(self, obj):
        return obj.profile.is_blocked
    is_blocked.boolean = True
    is_blocked.short_description = 'Blocked'

    def get_list_filter(self, request):
        return super().get_list_filter(request) + ('profile__is_blocked',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if 'is_blocked' in form.changed_data:
            obj.profile.is_blocked = form.cleaned_data['is_blocked']
            obj.profile.save()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)