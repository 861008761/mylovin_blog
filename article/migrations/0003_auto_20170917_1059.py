# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170917_1009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artilce',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time']},
        ),
    ]
