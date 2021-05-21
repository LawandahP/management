from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Bill


class UserBillsForm(forms.ModelForm):
    created_at = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Bill
        fields = ['unit', 'bill', 'amount', 'created_at']


class UserBillsSearchForm(forms.ModelForm):
    start_date = forms.DateField(widget=AdminDateWidget, required=True)
    end_date = forms.DateField(widget=AdminDateWidget, required=True)

    class Meta:
        model = Bill
        fields = ['start_date', 'end_date']
