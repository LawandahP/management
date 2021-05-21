import django_filters
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django_filters import DateFilter
from bill.models import Bill
from .models import *


class BillFilter(django_filters.FilterSet):
    month = DateFilter(field_name="date", lookup_expr='gte')
    year = DateFilter(field_name="date", lookup_expr='lte', widget=AdminDateWidget)

    class Meta:
        model = Bill
        fields = ['tenant', 'bill', 'amount', 'date']
        exclude = ['date']
