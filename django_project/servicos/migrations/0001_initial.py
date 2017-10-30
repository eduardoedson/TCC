# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True, verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
    ]
