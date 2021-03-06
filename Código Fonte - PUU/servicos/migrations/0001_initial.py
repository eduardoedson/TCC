# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True, verbose_name='Área de Atendimento')),
            ],
            options={
                'verbose_name_plural': 'Áreas de Atendimento',
                'ordering': ['setor', 'descricao'],
                'verbose_name': 'Área de Atendimento',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True, verbose_name='Nome da Disciplina')),
            ],
            options={
                'verbose_name_plural': 'Disciplinas',
                'ordering': ['descricao', 'setor'],
                'verbose_name': 'Disciplina',
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, unique=True, verbose_name='Nome do Setor')),
                ('nome', models.CharField(blank=True, max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Setores',
                'ordering': ['descricao'],
                'verbose_name': 'Setor',
            },
        ),
        migrations.AddField(
            model_name='disciplina',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Setor', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='areaatendimento',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Setor', verbose_name='Setor'),
        ),
    ]
