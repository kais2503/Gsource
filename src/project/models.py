from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    titre = models.CharField(max_length =120)
    description = models.TextField()
    date = models.DateField(auto_now=False,auto_now_add=False)

    def __unicode__(self):
        return self.description
    def __unicode__(self):
        return self.description
