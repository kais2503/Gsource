from __future__ import unicode_literals

from django.db import models

class Competition(models.Model):
    libelle=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField(auto_now=False,auto_now_add=False)
    lieu=models.CharField(max_length=80)

    def __unicode__(self):
        return self.libelle
