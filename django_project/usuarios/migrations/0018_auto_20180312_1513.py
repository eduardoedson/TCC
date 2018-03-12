# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-12 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_auto_20180312_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='area_atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.AreaAtendimento', verbose_name='Área de Atendimento'),
        ),
    ]
