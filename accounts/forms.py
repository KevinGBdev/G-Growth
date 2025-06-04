from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    cidade = forms.CharField()
    estado = forms.CharField()
    segmento = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
