from django import forms
from landlord.models import Landlord


class AddLandlordForm(forms.ModelForm):
    class Meta:
        model = Landlord
        fields = ['Full_Name', 'gender', 'email',
                  'National_ID', 'phone_number1', 'phone_number2',
                  'post_office_box']







