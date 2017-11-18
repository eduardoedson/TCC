# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 15:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_setor_nome'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0041_auto_20171104_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome Completo')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Nome de Usuário')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Setor', verbose_name='Setor Responsável')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recepcionistas',
                'verbose_name': 'Recepcionista',
                'ordering': ['nome', 'setor'],
            },
        ),
    ]
