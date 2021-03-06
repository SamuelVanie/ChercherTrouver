from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    numero_de_tel = models.CharField(max_length=13)
    numero_de_chambre = models.CharField(max_length = 3)
    genre = models.CharField(max_length = 1, choices = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
        ('A', 'Autre'),
    ]) 