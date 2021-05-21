from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from bill.models import Bill


class BillAdmin(BaseUserAdmin):
    list_display = ('bill', 'amount', 'unit', 'created_at',)
    list_filter = ('unit', 'created_at',)
    fieldsets = (
        (None, {'fields': ('bill', 'amount', 'unit', 'created_at',)}),
        ('Permissions', {'fields': ()}),
    )

    search_fields = ('bill',)
    ordering = ('created_at',)
    filter_horizontal = ()


admin.site.register(Bill, BillAdmin)


