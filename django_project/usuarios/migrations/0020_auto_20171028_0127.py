# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-28 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0019_fisioterapianeurologiainfantilavalicao_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisioterapianeurologiainfantilavalicao',
            name='anamnese_cirurgia_motivo',
            field=models.CharField(blank=True, max_length=50, verbose_name='Quais cirúrgias?'),
        ),
    ]
