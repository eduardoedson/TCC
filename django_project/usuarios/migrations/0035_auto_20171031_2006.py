# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0034_auto_20171030_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prontuario',
            name='paciente',
        ),
        migrations.DeleteModel(
            name='Prontuario',
        ),
    ]
