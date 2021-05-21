import django_filters
from unit.models import Unit


class UnitFilter(django_filters.filterset):
    class Meta:
        model = Unit
        fields = ['unit_no', 'unit_type',
                  'select_apartment', 'status']
