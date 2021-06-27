from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class add_form(models.Model):
   nom_objet = models.CharField(max_length=30)
   date_de_trouvaille = models.DateTimeField()
   description = models.TextField()
   author = models.ForeignKey(User, default=None, on_delete=False)
