from __future__ import unicode_literals

from django.db import models

class Media (models.Model):
    libelle=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    email=models.EmailField()
    responsable=models.CharField(max_length=80)
    genre=models.CharField(max_length=80)


    def __unicode__(self):
        return self.libelle
