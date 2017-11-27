# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0042_recepcionista'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisioterapiaAvaliacaoGestacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, verbose_name='Data da Avaliação')),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data de Nascimento')),
                ('idade', models.CharField(blank=True, max_length=40, verbose_name='Idade')),
                ('nome_pai', models.CharField(blank=True, max_length=40, verbose_name='Nome do Pai da Criança')),
                ('estado_civil', models.CharField(blank=True, max_length=40, verbose_name='Estado Civil')),
                ('profissao', models.CharField(blank=True, max_length=40, verbose_name='Profissão')),
                ('funcao', models.CharField(blank=True, max_length=40, verbose_name='Função')),
                ('endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('cep', models.CharField(blank=True, max_length=40, verbose_name='CEP')),
                ('telefone', models.CharField(blank=True, max_length=40, verbose_name='Telefone')),
                ('nome_bebe', models.CharField(blank=True, max_length=40, verbose_name='Nome do Bebê')),
                ('sexo_bebe', models.CharField(blank=True, choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo do Bebê')),
                ('anamnese_queixa_principal', models.TextField(blank=True, verbose_name='Queixa Principal')),
                ('gestacional_tipo_sangue', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], default='A', max_length=1, verbose_name='Tipagem Sanguínea')),
                ('gestacional_fator_rh', models.CharField(choices=[('-', '-'), ('+', '+')], default='+', max_length=1, verbose_name='Fator RH')),
                ('gestacional_dum', models.CharField(blank=True, max_length=40, verbose_name='DUM')),
                ('gestacional_dpp', models.CharField(blank=True, max_length=40, verbose_name='DPP')),
                ('gestacional_idade', models.CharField(blank=True, max_length=40, verbose_name='Idade Gestacional')),
                ('gestacional_data', models.CharField(blank=True, max_length=40, verbose_name='Data dos Primeiros Movimentos Fetais')),
                ('antecedentes_idade_menarca', models.CharField(blank=True, max_length=40, verbose_name='Idade da Menarca (Anos)')),
                ('antecedentes_idade_sexual', models.CharField(blank=True, max_length=40, verbose_name='Idade de Início da Atiidade Sexual (Anos)')),
                ('antecedentes_ciclo', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Sim', max_length=40, verbose_name='Regularidade do Ciclo Menstrual')),
                ('antecedentes_cirurgia', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Cirurgia ou Doença Ginecológica Anterior')),
                ('antecedentes_cirurgia_qual', models.CharField(blank=True, max_length=40, verbose_name='Qual?')),
                ('obstetrica_gestacao', models.CharField(blank=True, max_length=40, verbose_name='Número de Gestações Anteriores')),
                ('obstetrica_parto', models.CharField(choices=[('Normal', 'Normal'), ('Cesárea', 'Cesárea'), ('Fórceps', 'Usou Fórceps')], default='Norma', max_length=40, verbose_name='Tipo de Parto')),
                ('obstetrica_complicacao', models.CharField(blank=True, max_length=40, verbose_name='Complicações do Parto (Eclâmpsia e Pré-Eclâmpsia)')),
                ('obstetrica_prematuridade', models.CharField(blank=True, max_length=40, verbose_name='Prematuridade')),
                ('obstetrica_abortos', models.CharField(blank=True, max_length=40, verbose_name='Nº de Abortos')),
                ('obstetrica_doencas', models.CharField(blank=True, max_length=40, verbose_name='Doenças Associadas (DM? Hipertensão? IST?)')),
                ('obstetrica_medicacao', models.CharField(blank=True, max_length=40, verbose_name='Medicação')),
                ('doenca_cardiopatias', models.CharField(blank=True, max_length=40, verbose_name='Cardiopatias')),
                ('doenca_hipertensao', models.CharField(blank=True, max_length=40, verbose_name='Hipertensão')),
                ('doenca_epilepsia', models.CharField(blank=True, max_length=40, verbose_name='Epilepsia')),
                ('doenca_neoplasias', models.CharField(blank=True, max_length=40, verbose_name='Neoplasias')),
                ('doenca_diabetes', models.CharField(blank=True, max_length=40, verbose_name='Diabetes')),
                ('doenca_psiquicas', models.CharField(blank=True, max_length=40, verbose_name='Alterações Psíquicas')),
                ('doenca_malformacao', models.CharField(blank=True, max_length=40, verbose_name='Malformações')),
                ('infecciosas_tuberculose', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Tuberculose')),
                ('infecciosas_sifilis', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Sífilis')),
                ('infecciosas_rubeola', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Rubéola')),
                ('infecciosas_tuxoplasmose', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Tuxoplasmose')),
                ('infecciosas_sarampo', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Sarampo')),
                ('infecciosas_hepatite', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Hepatite')),
                ('habitos_tabagismo', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Tabagismo')),
                ('habitos_etilismo', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Etilismo')),
                ('habitos_drogas', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Drogas')),
                ('habitos_alimentacao', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Alimentação')),
                ('habitos_medicamentos', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Medicamentos')),
                ('historia_frequencia_diurno', models.CharField(blank=True, max_length=40, verbose_name='Frequência da Micção (Diurno)')),
                ('historia_frequencia_noturno', models.CharField(blank=True, max_length=40, verbose_name='Frequência da Micção (Noturno)')),
                ('historia_frequencia_total', models.CharField(blank=True, max_length=40, verbose_name='Frequência da Micção (Total)')),
                ('historia_perda', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Tem perda de urina?')),
                ('historia_perda_total', models.CharField(blank=True, max_length=40, verbose_name='Casos de Perda da Urina')),
                ('historia_perda_tempo', models.CharField(blank=True, choices=[('Após as atividades', 'Após as atividades'), ('Ao mesmo tempo que as atividades', 'Ao mesmo tempo que as atividades')], max_length=40, verbose_name='Quando Ocorre Perda de Urina?')),
                ('historia_perda_comeco', models.CharField(blank=True, choices=[('Durante gestação', 'Durante gestação'), ('Depois da gestação', 'Depois da gestação'), ('Após cirurgia vaginal/abdominal', 'Após cirurgia vaginal/abdominal'), ('Depois da cesariana', 'Depois da cesariana')], max_length=40, verbose_name='Quando Começou a Perda de Urina?')),
                ('historia_vontade', models.CharField(blank=True, choices=[('Urgente', 'Urgente'), ('Controlada', 'Controlada')], max_length=40, verbose_name='Como é a vontade de urinar?')),
                ('historia_dor', models.CharField(choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=40, verbose_name='Existe Dor ao Urinar?')),
                ('historia_urina_cor', models.CharField(blank=True, max_length=40, verbose_name='Cor da Urina')),
                ('historia_urina_odor', models.CharField(blank=True, max_length=40, verbose_name='Odor da Urina')),
                ('exame_pa', models.CharField(blank=True, max_length=40, verbose_name='PA')),
                ('exame_fc', models.CharField(blank=True, max_length=40, verbose_name='FC')),
                ('exame_t', models.CharField(blank=True, max_length=40, verbose_name='T')),
                ('exame_fr', models.CharField(blank=True, max_length=40, verbose_name='FR')),
                ('exame_respiracao', models.CharField(blank=True, max_length=40, verbose_name='Tipo de Respiração')),
                ('seios_volume', models.CharField(blank=True, choices=[('Aumentado', 'Aumentado'), ('Normal', 'Normal'), ('Diminuído', 'Diminuído')], max_length=40, verbose_name='Volume')),
                ('seios_temperatura', models.CharField(blank=True, choices=[('Aumentada', 'Aumentada'), ('Normal', 'Normal'), ('Diminuída', 'Diminuída')], max_length=40, verbose_name='Temperatura')),
                ('seios_circulacao', models.CharField(blank=True, choices=[('Aumentada', 'Aumentada'), ('Normal', 'Normal'), ('Diminuída', 'Diminuída')], max_length=40, verbose_name='Circulação Cutânea')),
                ('seios_mamilo', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Raso', 'Raso'), ('Invertido', 'Invertido')], max_length=40, verbose_name='Tipo de Mamilo')),
                ('seios_colostro', models.CharField(blank=True, choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=40, verbose_name='Colostro')),
                ('seios_estrias', models.CharField(blank=True, choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=40, verbose_name='Estrias')),
                ('seios_hiperpigmentacao', models.CharField(blank=True, choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=40, verbose_name='Hiperpigmentação')),
                ('abdomem_hiperpigmentacao', models.CharField(blank=True, choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=40, verbose_name='Hiperpigmentação')),
                ('abdomem_volume', models.CharField(blank=True, choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=40, verbose_name='Aumento de Volume')),
                ('abdomem_estrias', models.CharField(blank=True, choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=40, verbose_name='Estrias')),
                ('abdomem_cicatriz', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Herniada', 'Herniada'), ('Plana', 'Plana')], max_length=40, verbose_name='Cicatriz')),
                ('abdomem_altura', models.CharField(blank=True, max_length=40, verbose_name='Altura Uterina')),
                ('abdomem_circuferencia', models.CharField(blank=True, max_length=40, verbose_name='Circuferência Abdominal')),
                ('mmii_edema', models.CharField(blank=True, max_length=40, verbose_name='Edema')),
                ('mmii_varizes', models.CharField(blank=True, max_length=40, verbose_name='Varizes')),
                ('mmii_caimbras', models.CharField(blank=True, max_length=40, verbose_name='Câimbras')),
                ('mmii_dor', models.CharField(blank=True, max_length=40, verbose_name='Dor')),
                ('musculo_palpacao', models.CharField(blank=True, max_length=40, verbose_name='Palpação do Períneo')),
                ('musculo_contracao', models.CharField(blank=True, max_length=40, verbose_name='Tempo de Contração')),
                ('testes_especiais', models.TextField(blank=True, verbose_name='Testes Especiais')),
                ('diagnostico', models.TextField(blank=True, verbose_name='Diagnóstico Fisioterapêutico')),
                ('metas', models.TextField(blank=True, verbose_name='Metas a Curto e Longo Prazo')),
                ('recursos', models.TextField(blank=True, verbose_name='Recursos Que Serão Utilizados Como Justificativa')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Avaliação Fisioterapêutica Gestacional',
                'verbose_name_plural': 'Avaliações Fisioterapêutica Gestacional',
                'ordering': ['data'],
            },
        ),
    ]