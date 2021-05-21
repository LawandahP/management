from django.contrib import admin
from landlord.models import Landlord


class LandlordAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'National_ID', 'phone_number1', 'created_at')
    list_filter = ('gender',)
    search_fields = ('Full_Name',)


admin.site.register(Landlord, LandlordAdmin)
