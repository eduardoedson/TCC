# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-28 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0023_auto_20171028_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='area_atendimento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='servicos.AreaAtendimento', verbose_name='Área de Atendimento'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='atividade_fisica',
            field=models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=10, verbose_name='Pratica atividade física?'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='atividade_laboral',
            field=models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=10, verbose_name='Pratica atividade laboral?'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='data_laudo',
            field=models.DateField(blank=True, verbose_name='Data Laudo Médico'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='diagnostico',
            field=models.TextField(blank=True, verbose_name='Diagnóstico Clínico'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='exames_complementares',
            field=models.TextField(blank=True, verbose_name='Exames Complementares'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='paciente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='parecer',
            field=models.TextField(blank=True, verbose_name='Parecer para atendimento'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='patologia',
            field=models.TextField(blank=True, verbose_name='Patologias Associadas'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='queixa_principal',
            field=models.TextField(blank=True, verbose_name='Queixa Principal'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='relato',
            field=models.TextField(blank=True, verbose_name='Relato do Paciente'),
        ),
        migrations.AlterField(
            model_name='fisioterapiatriagem',
            name='uso_medicamentos',
            field=models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=10, verbose_name='Faz uso de medicamentos?'),
        ),
    ]
