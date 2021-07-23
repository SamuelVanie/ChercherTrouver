from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCustomForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['numero_de_tel', 'numero_de_chambre', 'genre']
