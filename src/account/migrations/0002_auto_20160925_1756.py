# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='Images/user.png', upload_to='Images/'),
        ),
    ]