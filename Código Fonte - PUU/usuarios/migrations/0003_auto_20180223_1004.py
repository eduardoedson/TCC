# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-23 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20180223_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='valor_aluguel',
            field=models.CharField(blank=True, choices=[('Alugada', 'Alugada'), ('Propria', 'Própria')], max_length=30, verbose_name='Se alugada, Valor'),
        ),
    ]
