from django import forms
from django.contrib.auth import get_user_model
custom_user_model = get_user_model()


class CustomUserLoginForm(forms.Form):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    username = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(max_length=100, 
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    class Meta:
        model = custom_user_model
        fields = ('username', 'password')

