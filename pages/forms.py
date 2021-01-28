from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from profiles import models as profile_models


class SignupForm(ModelForm):
    """user signup form"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')
        widgets = {
        'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    """user login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_type'].label = 'Register As'
    """user Profile form"""
    class Meta:
        model = profile_models.Profile
        fields = ('mobile', 'gender', 'profile_type', 'district')
        # widgets = {
        # 'profile_type': verbose_name ,
        # }