# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20171027_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='beneficio',
            field=models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], default='Não', max_length=10, verbose_name='Possui beneficio do governo?'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='colaborador',
            field=models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], default='Não', max_length=10, verbose_name='Colaborador da instituição?'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tratamento_sus',
            field=models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], default='Não', max_length=10, verbose_name='Realiza tratamento pelo SUS?'),
        ),
    ]
