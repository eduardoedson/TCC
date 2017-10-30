# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0007_areaatendimento'),
        ('usuarios', '0014_auto_20171027_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisioterapiaTriagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_triagem', models.DateField(auto_now_add=True, verbose_name='Data Triagem')),
                ('data_laudo', models.DateField(verbose_name='Data Laudo Médico')),
                ('avds_independente', models.CharField(blank=True, max_length=30, verbose_name="AVD'S Independente")),
                ('tempo_lesao', models.CharField(blank=True, max_length=30, verbose_name='Tempo de Lesão')),
                ('marcha_independente', models.CharField(blank=True, max_length=30, verbose_name='Marcha Independente')),
                ('cid', models.CharField(blank=True, max_length=30, verbose_name='CID')),
                ('uso_medicamentos', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Faz uso de medicamentos?')),
                ('atividade_fisica', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Pratica atividade física?')),
                ('atividade_laboral', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Pratica atividade laboral?')),
                ('relato', models.TextField(verbose_name='Relato do Paciente')),
                ('diagnostico', models.TextField(verbose_name='Diagnóstico Clínico')),
                ('queixa_principal', models.TextField(verbose_name='Queixa Principal')),
                ('patologia', models.TextField(verbose_name='Patologias Associadas')),
                ('tratamento_anterior', models.TextField(blank=True, verbose_name='Tratamento Anterior')),
                ('exames_complementares', models.TextField(verbose_name='Exames Complementares')),
                ('parecer', models.TextField(verbose_name='Parecer para atendimento')),
                ('area_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.AreaAtendimento', verbose_name='Área de Atendimento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name_plural': 'Triagens de Fisioterapia ',
                'verbose_name': 'Triagem de Fisioterapia',
                'ordering': ['data_triagem'],
            },
        ),
    ]