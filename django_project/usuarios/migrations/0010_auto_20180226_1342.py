# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-26 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20180226_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisioterapiaavaliacaogestacional',
            name='gestacional_data',
            field=models.DateField(blank=True, verbose_name='Data dos Primeiros Movimentos Fetais'),
        ),
        migrations.AlterField(
            model_name='fisioterapiaavaliacaogestacional',
            name='gestacional_tipo_sangue',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2, verbose_name='Tipagem Sanguínea'),
        ),
    ]
