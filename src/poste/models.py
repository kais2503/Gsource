from __future__ import unicode_literals

from django.db import models

class poste (models.Model):

    libelle= models.CharField(max_length=100)
    def __unicode__(self):
        return self.libelle
