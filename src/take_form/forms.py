from django import forms 
from .models import take_form
from django.forms import ModelForm

class TakeObjectForm(forms.ModelForm):
    class Meta:
        model = take_form
        fields = ['nom','numero_de_telephone','numero_de_chambre','date_de_perte', 'description']
