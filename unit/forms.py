from django import forms
from unit.models import Unit, AllocateTenantUnit, VacateTenant
from users.models import CustomUser
from django.contrib.admin.widgets import AdminDateWidget


class AddUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['select_apartment', 'unit_no',
                  'unit_type', 'rent', ]


class AllocateTenantUnitForm(forms.ModelForm):
    placement_date = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = AllocateTenantUnit
        fields = ['select_apartment', 'unit_no', 'unit_type',
                  'rent', 'tenant', 'deposit', 'rent_paid',
                  'placement_date', 'confirm_allocation'
                  ]


class VacateTenantForm(forms.ModelForm):
    class Meta:
        model = VacateTenant
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['tenant'].queryset = CustomUser.objects.none()

