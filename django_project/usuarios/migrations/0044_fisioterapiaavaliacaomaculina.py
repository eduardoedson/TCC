# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0043_fisioterapiaavaliacaogestacional'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisioterapiaAvaliacaoMaculina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, verbose_name='Data da Avaliação')),
                ('data_atendimento', models.DateField(blank=True, verbose_name='Data do Atendimento')),
                ('registro', models.CharField(blank=True, max_length=40, verbose_name='Registro')),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data de Nascimento')),
                ('idade', models.CharField(blank=True, max_length=40, verbose_name='Idade')),
                ('estado_civil', models.CharField(blank=True, max_length=40, verbose_name='Estado Civil')),
                ('profissao', models.CharField(blank=True, max_length=40, verbose_name='Profissão')),
                ('funcao', models.CharField(blank=True, max_length=40, verbose_name='Função')),
                ('endereco', models.CharField(blank=True, max_length=40, verbose_name='Endereço')),
                ('cep', models.CharField(blank=True, max_length=40, verbose_name='CEP')),
                ('telefone', models.CharField(blank=True, max_length=40, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, max_length=40, verbose_name='Celular')),
                ('motivo', models.TextField(blank=True, verbose_name='Motivo da Consulta')),
                ('antecedentes_altura', models.CharField(blank=True, max_length=40, verbose_name='Altura')),
                ('antecedentes_imc', models.CharField(blank=True, max_length=40, verbose_name='IMC')),
                ('antecedentes_intestino', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Obstipado', 'Obstipado')], max_length=40, verbose_name='Intestino')),
                ('antecedentes_infeccoes', models.CharField(blank=True, choices=[('Anteriores', 'Anteriores'), ('Repetições', 'Repetições'), ('Atual', 'Atual')], max_length=40, verbose_name='Infecções')),
                ('antecedentes_freq_miccional', models.CharField(blank=True, choices=[('Diurna', 'Diurna'), ('Noturna', 'Noturna')], max_length=40, verbose_name='Frequência Miccional')),
                ('antecedentes_esvaziamento', models.CharField(blank=True, choices=[('Completo', 'Completo'), ('Incompleto', 'Incompleto')], max_length=40, verbose_name='Sensação de Esvaziamento Vesical')),
                ('antecedentes_gotejamento', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Gotejamento Pós-Miccional')),
                ('antecedentes_urgencia', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Urgência Miccional')),
                ('antecedentes_perda', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Sensação de Perda')),
                ('antecedentes_iue', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='IUE')),
                ('antecedentes_tosse', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Tosse')),
                ('antecedentes_espirro', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Espirro')),
                ('antecedentes_riso', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Riso Forçado')),
                ('antecedentes_atividade', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Atividade Física')),
                ('antecedentes_esporte', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Esporte')),
                ('antecedentes_sexual', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Relação Sexual')),
                ('antecedentes_marcha', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Marcha')),
                ('antecedentes_corrida', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Corrida')),
                ('antecedentes_peso', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Carregamento de Peso')),
                ('antecedentes_posicao', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Mudança de Posição')),
                ('antecedentes_forros', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Troca de Forros')),
                ('antecedentes_cigarro', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Cigarro')),
                ('antecedentes_alcool', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Álcool')),
                ('antecedentes_habitos', models.TextField(blank=True, verbose_name='Hábitos de Vida')),
                ('antecedentes_cirurgia', models.TextField(blank=True, max_length=40, verbose_name='Cirurgias Anteriores')),
                ('antecedentes_medicacoes', models.TextField(blank=True, verbose_name='Medicações Atuais')),
                ('doencas_atuais', models.TextField(blank=True, verbose_name='Doenças Atuais')),
                ('doencas_neurologicas', models.TextField(blank=True, verbose_name='Doenças Neurológicas')),
                ('doencas_ortopedicas', models.TextField(blank=True, verbose_name='Doenças Ortopédicas')),
                ('doencas_psiquiatricas', models.TextField(blank=True, verbose_name='Doenças Psiquiátricas')),
                ('doencas_bronquite_tosse', models.TextField(blank=True, verbose_name='Bronquite ou Tosse')),
                ('doencas_diabetes', models.TextField(blank=True, verbose_name='Diabetes')),
                ('doencas_gerais', models.TextField(blank=True, verbose_name='Doenças Gerais')),
                ('doencas_satisfacao', models.CharField(blank=True, choices=[('Satisfeito', 'Satisfeito'), ('Insatisfeito', 'Insatisfeito'), ('Indiferente', 'Indiferente')], max_length=40, verbose_name='Grau de Satisfação com a Situação Atual')),
                ('dados_urodinamicos', models.TextField(blank=True, verbose_name='Pré-Tratamento - Considerar Resultados Médicos')),
                ('exame_fisico', models.TextField(blank=True, verbose_name='Avaliação Postural')),
                ('exame_pele', models.CharField(blank=True, choices=[('Atrófica', 'Atrófica'), ('Normal', 'Normal')], max_length=40, verbose_name='Estado da Pele')),
                ('exame_pele_inspecao', models.CharField(blank=True, choices=[('Mucosa Hipeêmica', 'Mucosa Hipeêmica'), ('Presença de irritação local', 'Presença de irritação local '), ('Presença de Corrimentos', 'Presença de Corrimentos'), ('Presença de cicatrizes', 'Presença de cicatrizes'), ('Presença de Varicosidades', 'resença de Varicosidades')], max_length=40, verbose_name='Inspeção da Pele')),
                ('exame_cicatriz', models.CharField(blank=True, max_length=40, verbose_name='Cicatrizes/Aderências')),
                ('exame_zonas', models.CharField(blank=True, max_length=40, verbose_name='Zonas Doloras')),
                ('exame_hernias', models.CharField(blank=True, max_length=40, verbose_name='Hérnias')),
                ('exame_diastase', models.CharField(blank=True, max_length=40, verbose_name='Diástase')),
                ('exame_nucleo_fibroso', models.CharField(blank=True, choices=[('Hipotônico (Depressão)', 'Hipotônico (Depressão)'), ('Normal (Resist. Elástica)', 'Normal (Resist. Elástica)'), ('Hipertônico (Resist. Rígida)', 'Hipertônico (Resist. Rígida)')], max_length=40, verbose_name='Núcleo Fibroso Central do Príneo')),
                ('exame_forca', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=40, verbose_name='Força Muscular')),
                ('avaliacao_funcional', models.CharField(blank=True, choices=[('Grau 0', 'Sem função perineal objetiva, nem mesmo à palpitação'), ('Grau 1', 'Função perineal objetiva ausente, contração reconhecível somente à palpação.'), ('Grau 2', 'Função perineal objetiva débil, reconhecida à palpação.'), ('Grau 3', 'Função perineal objetiva presente e resistência opositora à palpação; não mantida'), ('Grau 4', 'Função perineal objetiva presente e resistência opositora mantida mais que cinco segundos')], max_length=40, verbose_name='AFA')),
                ('avaliacao_apneia', models.CharField(blank=True, choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], max_length=40, verbose_name='Apneia')),
                ('avaliacao_participacao', models.CharField(blank=True, choices=[('Abdominais', 'Abdominais'), ('Glúteos', 'Glúteos'), ('Adutores', 'Adutores')], max_length=40, verbose_name='Participação de Músculos Acessórios')),
                ('avaliacao_testes', models.TextField(blank=True, verbose_name='Testes Especiais (Se Houver Necessidade)')),
                ('avaliacao_diagnostico', models.TextField(blank=True, verbose_name='Diagnóstico Fisioterapêutico')),
                ('avaliacao_metas', models.TextField(blank=True, verbose_name='Metas a Curto e Longo Prazo')),
                ('avaliacao_recursos', models.TextField(blank=True, verbose_name='Recursos Que Serão Utilizados Com Justificativa')),
                ('aluno', models.CharField(blank=True, max_length=40, verbose_name='Nome do Aluno')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Avaliações de Incontinência Urinária Masculina',
                'ordering': ['data'],
                'verbose_name': 'Avaliação de Incontinência Urinária Masculina',
            },
        ),
    ]