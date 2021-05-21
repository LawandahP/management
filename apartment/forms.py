from django import forms

from apartment.models import Apartment


class AddApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'type', 'county', 'location',
                  'location_description', 'owner']
