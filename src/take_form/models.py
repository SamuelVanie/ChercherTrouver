from django.db import models
from objects.models import objetPerdu

class take_form(models.Model):
    nom = models.CharField(max_length=12)
    numero_de_telephone = models.CharField(max_length=13)
    numero_de_chambre = models.CharField(max_length=3)
    date_de_perte = models.DateField()
    description = models.TextField()
    objet = models.ForeignKey(objetPerdu, on_delete=False, default=None)
