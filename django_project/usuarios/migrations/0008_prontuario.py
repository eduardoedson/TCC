# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20170815_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico', models.CharField(max_length=50, verbose_name='Médico')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data Consulta')),
                ('hora', models.CharField(max_length=5, verbose_name='Hora Consulta')),
                ('arq_1', models.FileField(blank=True, upload_to=usuarios.models.media_path, verbose_name='Arquivo 1')),
                ('arq_2', models.FileField(blank=True, upload_to=usuarios.models.media_path, verbose_name='Arquivo 2')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Prontuário',
                'verbose_name_plural': 'Prontuários',
                'ordering': ['paciente', 'data'],
            },
        ),
    ]