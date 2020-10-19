from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)  # username determined by email so case ID

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # deleted username


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    # username = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUPdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#class ApplyForm(forms.ModelForm):
    #reason, resume, contact_info

