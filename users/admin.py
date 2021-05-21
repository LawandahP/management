from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import CustomUser, Profile


class UserAdmin(BaseUserAdmin):
    list_display = ('Tenant_Full_Names', 'username', 'email', 'is_staff',
                    'is_admin', 'is_tenant', 'is_active')
    list_filter = ('is_admin', 'is_tenant')
    fieldsets = (
        (None, {'fields': ('Tenant_Full_Names', 'email', 'gender',
                           'National_ID', 'phone_number1', 'phone_number2',
                           'occupation_status', 'at')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_tenant',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'Tenant_Full_Names', 'email', 'gender',
                       'National_ID', 'phone_number1', 'phone_number2',
                       'occupation_status', 'at', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('date_joined',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)


class ProfileAdmin(BaseUserAdmin):
    list_display = ('user', 'image', 'marital_status',)
    list_filter = ('marital_status',)
    fieldsets = (
        (None, {'fields': ('user', 'image', 'marital_status',)}),
        ('Permissions', {'fields': ()}),
    )

    search_fields = ('user', 'marital_status')
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(Profile, ProfileAdmin)
