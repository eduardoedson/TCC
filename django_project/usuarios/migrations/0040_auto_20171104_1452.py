# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0039_auto_20171104_1441'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coordenador',
            new_name='Supervisor',
        ),
        migrations.AlterModelOptions(
            name='supervisor',
            options={'ordering': ['nome', 'setor'], 'verbose_name': 'Supervisor (a)', 'verbose_name_plural': 'Supervisores (as)'},
        ),
    ]