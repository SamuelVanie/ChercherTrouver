from django import forms 
from .models import add_form 
from django.forms import ModelForm


class AddObjectForm(forms.ModelForm):
    class Meta:
        model = add_form
        fields = ['nom_objet', 'date_de_trouvaille', 'description']
