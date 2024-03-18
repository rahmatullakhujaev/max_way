from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(widget= forms.PasswordInput(attrs= {
        "class": "form-control",
        "placeholder": "Enter your password"
    }))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs= {
        "class": "form-control",
        "placeholder": "Retype your password"

    }))
    class Meta:
        model = User
        fields = ['phone_number', 'username']
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "input", "placeholder": "Create new username"

            }),
            "phone_number": forms.TextInput(attrs={
                "class": "input", "placeholder": "Enter your phone number"
            })
        }

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(widget= forms.PasswordInput(attrs= {
        "class": "input",
        "placeholder": "Enter your password"
    }))
