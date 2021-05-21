from django import forms

from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime


class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'Tenant_Full_Names',
                  'email', 'gender', 'National_ID', 'phone_number1', 'phone_number2',
                  'occupation_status', 'at', 'password1', 'password2']


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'Tenant_Full_Names', 'email', 'gender',
                  'National_ID', 'phone_number1', 'phone_number2',
                  'occupation_status', 'at']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number1', 'phone_number2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'marital_status']



