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
    #email = forms.EmailField(required=True)



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class ProfileUPdateForm(forms.ModelForm):
    resume = forms.FileField(required=False)
    class Meta:
        model = Profile
        fields = ['image', 'resume']




