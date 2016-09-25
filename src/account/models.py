from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Account(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Images/',default='Images/user.png')
    date=models.DateField(auto_now=True,auto_now_add=False)

    def __unicode__(self):

        return self.user.first_name
