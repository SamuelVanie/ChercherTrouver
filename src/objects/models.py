from django.db import models

# Create your models here.
class objetPerdu(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"{self.id}/"
