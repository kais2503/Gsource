from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    libelle=models.CharField(max_length = 100)
    description=models.TextField()
    email=models.EmailField()
    adresse=models.CharField(max_length =100)
    siteweb=models.CharField(max_length =100)
    facebookpage=models.CharField(max_length =100)

    def __unicode__(self):
        return self.libelle
