# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-14 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_auto_20180312_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisioterapiageriatriaanamnese',
            name='cuidar_casa',
            field=models.CharField(choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não', max_length=20, verbose_name='Cuidar da Casa?'),
        ),
        migrations.AlterField(
            model_name='fisioterapiageriatriaanamnese',
            name='jardinagem',
            field=models.CharField(choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não', max_length=20, verbose_name='Jardinagem?'),
        ),
        migrations.AlterField(
            model_name='fisioterapiageriatriaanamnese',
            name='lavar_roupa',
            field=models.CharField(choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não', max_length=20, verbose_name='Lavar Roupa?'),
        ),
        migrations.AlterField(
            model_name='fisioterapiageriatriaanamnese',
            name='passar_roupa',
            field=models.CharField(choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não', max_length=20, verbose_name='Passar Roupa?'),
        ),
        migrations.AlterField(
            model_name='fisioterapiageriatriaanamnese',
            name='supermecado',
            field=models.CharField(choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não', max_length=20, verbose_name='Ir ao supermecado?'),
        ),
    ]
