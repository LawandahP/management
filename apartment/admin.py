from django.contrib import admin
from apartment.models import Apartment


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'county', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name',)


admin.site.register(Apartment, ApartmentAdmin)
