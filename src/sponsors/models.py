from __future__ import unicode_literals

from django.db import models

class Sponsor (models.Model):

    libelle = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    domaine = models.CharField(max_length=100)
    pack = models.CharField(max_length=80)
    website = models.CharField(max_length=80)
    facebookpage = models.CharField(max_length=80)
    responsable = models.CharField(max_length=80)

    def __unicode__(self):
        return self.libelle
