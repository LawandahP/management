from .models import Unit, AllocateTenantUnit
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_no', 'unit_type', 'select_apartment', 'rent', 'created_at')
    list_filter = ('select_apartment', 'unit_type',)
    search_fields = ('unit_no',)


admin.site.register(AllocateTenantUnit)
admin.site.register(Unit, UnitAdmin)
