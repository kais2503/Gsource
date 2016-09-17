from __future__ import unicode_literals

from django.db import models

class Conferencier (models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    domaine=models.CharField(max_length=150)

    def __unicode__ (self):
        return self.nom
