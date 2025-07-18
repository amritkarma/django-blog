from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User, Profile
from accounts.forms import UserCreationForm, UserChangeForm

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_active',
                    'is_staff', 'is_superuser',)
    list_filter = ('is_active', 'is_staff', 'is_superuser',
                   'date_joined',)
    readonly_fields = ('date_joined', 'last_login',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        ('Personal Info', {
         'fields': ('first_name', 'last_name', 'phone_no',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Email Phone Verification', {
         'fields': ('is_email_verified', 'is_phone_verified',)}),
        ('Important Date', {'fields': ('date_joined', 'last_login')}),
    )

    add_fieldsets = (
        (None,
            {'classes': ('wide'),
             'fields': ('username', 'email', 'password1', 'password2', 'phone_no',),
             }),
    )

    search_fields = ('username', 'email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'user', 'slug', 'is_verified',)
    list_display_links = ('user_username', 'user', 'slug',)
    readonly_fields = ('user', 'slug',)

    def user_username(self, obj):
        return obj.user.username

