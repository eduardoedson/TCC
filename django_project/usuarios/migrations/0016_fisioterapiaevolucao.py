# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_fisioterapiatriagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisioterapiaEvolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name_plural': 'Evoluções',
                'verbose_name': 'Evolução',
                'ordering': ['data'],
            },
        ),
    ]