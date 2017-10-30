# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-28 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_fisioterapiaevolucao'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisioterapiaNeurologiaInfantilAvalicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('data', models.DateField(verbose_name='Data')),
                ('responsavel', models.CharField(max_length=50, verbose_name='Responsável')),
                ('idade', models.CharField(max_length=50, verbose_name='Idade')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('medico', models.CharField(max_length=50, verbose_name='Médico Responsável')),
                ('diagnostico', models.TextField(verbose_name='Diagnóstico Clínico')),
                ('historio_comprimento', models.CharField(max_length=50, verbose_name='Comprimento')),
                ('historio_peso', models.CharField(max_length=50, verbose_name='Peso')),
                ('historio_pc', models.CharField(max_length=50, verbose_name='P.C.')),
                ('historio_apgar', models.CharField(max_length=50, verbose_name='Apgar')),
                ('anamnese_atitude', models.CharField(choices=[('Passiva', 'Passiva'), ('Hipoativa', 'Hipoativa'), ('Ativa', 'Ativa')], max_length=10, verbose_name='Atitude')),
                ('anamnese_escola', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Frequenta Escola?')),
                ('anamnese_escola_motivo', models.CharField(blank=True, max_length=50, verbose_name='Frequenta Escola? Justificativa')),
                ('anamnese_fisioterapia', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Realiza fisioterapia?')),
                ('anamnese_comunicacao', models.CharField(max_length=50, verbose_name='Comunicação')),
                ('anamnese_convulsao', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Convulsões?')),
                ('anamnese_convulsao_motivo', models.CharField(blank=True, max_length=50, verbose_name='Convulsões? Frequência')),
                ('anamnese_medicamentos', models.TextField(blank=True, verbose_name='Medicamentos')),
                ('anamnese_constipacao', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Constipação')),
                ('anamnese_sialorreia', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Sialorréia')),
                ('anamnese_refluxo', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Refluxo')),
                ('anamnese_dor', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Dor?')),
                ('anamnese_dor_motivo', models.CharField(blank=True, max_length=50, verbose_name='Quais dores?')),
                ('anamnese_visao', models.CharField(choices=[('Sem alteração', 'Sem alteração'), ('Deficiência', 'Deficiência')], max_length=10, verbose_name='Visão')),
                ('anamnese_cirurgia', models.CharField(choices=[(None, '----'), ('Sim', 'Não'), ('Não', 'Sim')], max_length=10, verbose_name='Interveções Cirúrgica?')),
                ('anamnese_cirurgia_motivo', models.CharField(blank=True, max_length=50, verbose_name='Quais cirgias?')),
                ('anamnese_avd', models.CharField(choices=[('Sem alteração', 'Sem alteração'), ('Deficiência', 'Deficiência')], max_length=10, verbose_name='AVD')),
                ('queixa_principal', models.TextField(blank=True, verbose_name='Queixa Principal')),
                ('exame_pele', models.CharField(blank=True, max_length=10, verbose_name='Pele')),
                ('exame_edema', models.CharField(blank=True, max_length=10, verbose_name='Edema')),
                ('exame_cicatrizes', models.CharField(blank=True, max_length=10, verbose_name='Cicatrizes')),
                ('exame_tonus', models.CharField(blank=True, max_length=10, verbose_name='Tônus/Trofismo Muscular')),
                ('exame_reflexos', models.CharField(blank=True, max_length=10, verbose_name='Reflexos')),
                ('exame_deformidades', models.CharField(blank=True, max_length=10, verbose_name='Deformidades')),
                ('exame_complementares', models.CharField(blank=True, max_length=10, verbose_name='Exames Complementares')),
                ('exame_aquisicao_motora', models.CharField(blank=True, max_length=10, verbose_name='Exames Aquisições Motoras')),
                ('exame_diagnostico', models.CharField(blank=True, max_length=10, verbose_name='Diagnóstico Fisioterapêutico')),
                ('exame_proposta', models.CharField(blank=True, max_length=10, verbose_name='Proposta Fisioterapêutico')),
                ('exame_observacao', models.CharField(blank=True, max_length=10, verbose_name='Observações Importantes')),
            ],
            options={
                'verbose_name': 'Avaliação Fisioterápica em Neuropediatria',
                'ordering': ['data'],
                'verbose_name_plural': 'Avaliações Fisioterápica em Neuropediatria',
            },
        ),
    ]