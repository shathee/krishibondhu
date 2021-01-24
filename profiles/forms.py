from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }

class ProfileForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ('gender', 'profile_type', 'mobile')
        widgets = {
            "gender": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "profile_type": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }