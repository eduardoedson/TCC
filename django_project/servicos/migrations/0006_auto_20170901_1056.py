# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0005_auto_20170812_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplina',
            options={'ordering': ['descricao', 'setor'], 'verbose_name': 'Disciplina', 'verbose_name_plural': 'Disciplinas'},
        ),
    ]