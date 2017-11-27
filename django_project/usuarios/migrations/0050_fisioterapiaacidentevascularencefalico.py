# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0049_auto_20171118_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisioterapiaAcidenteVascularEncefalico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, verbose_name='Data da Avaliação')),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data de Nascimento')),
                ('idade', models.CharField(blank=True, max_length=40, verbose_name='Idade')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('endereco', models.CharField(blank=True, max_length=40, verbose_name='Endereço')),
                ('telefone', models.CharField(blank=True, max_length=40, verbose_name='Telefone')),
                ('profissao', models.CharField(blank=True, max_length=40, verbose_name='Profissão')),
                ('estado_civil', models.CharField(blank=True, max_length=40, verbose_name='Estado Civil')),
                ('diagnostico_clinico', models.CharField(blank=True, max_length=40, verbose_name='Diagnóstico Clínico')),
                ('diagnostico_fisioterapico', models.CharField(blank=True, max_length=40, verbose_name='Diagnóstico Fisioterápico')),
                ('dados_pa', models.CharField(blank=True, max_length=40, verbose_name='P.A.')),
                ('dados_fc', models.CharField(blank=True, max_length=40, verbose_name='F.C.')),
                ('dados_fr', models.CharField(blank=True, max_length=40, verbose_name='F.R.')),
                ('dados_t', models.CharField(blank=True, max_length=40, verbose_name='T°')),
                ('medicamentos_utilizados', models.TextField(blank=True, verbose_name='Medicamentos Utilizados')),
                ('patologias_hipertensao', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=1, verbose_name='Hipertensão Arterial')),
                ('patologias_cardiopatias', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=1, verbose_name='Cardiopatias')),
                ('patologias_diabetes', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=1, verbose_name='Diabetes')),
                ('patologias_articular', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=1, verbose_name='Comprometimento Articular')),
                ('patologias_alergias', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=1, verbose_name='Alergias')),
                ('patologias_dor', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=1, verbose_name='Dor')),
                ('patologias_outras', models.TextField(blank=True, verbose_name='Outras')),
                ('patologias_cirurgico', models.TextField(blank=True, verbose_name='Antecedentes Cirúrgicos')),
                ('anamnese_qp', models.TextField(blank=True, verbose_name='Q.P.')),
                ('anamnese_lesao', models.CharField(blank=True, max_length=40, verbose_name='H.M.P.A.: Tempo da Lesão')),
                ('anamnese_tratamento', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Tratamento Fisioterápico')),
                ('exame_atitude', models.CharField(blank=True, choices=[('Ativo', 'Ativo'), ('Passivo', 'Passivo')], max_length=40, verbose_name='Atitude')),
                ('exame_consciencia', models.CharField(blank=True, choices=[('Bom', 'Bom'), ('Regular', 'Regular'), ('Ruim', 'Ruim')], max_length=40, verbose_name='Nível de Consciência')),
                ('exame_postura', models.TextField(blank=True, verbose_name='Postura')),
                ('exame_marcha', models.TextField(blank=True, verbose_name='Exame da Marcha')),
                ('exame_retracao_encurtamento', models.TextField(blank=True, verbose_name='Retrações e Encurtamentos')),
                ('exame_deformidades', models.TextField(blank=True, verbose_name='Deformidades')),
                ('movimentos_coreia', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Coréia')),
                ('movimentos_atetose', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Atetose')),
                ('movimentos_balismo', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Balismo')),
                ('movimentos_tremor', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Tremor')),
                ('movimentos_mioclonia', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Mioclonias')),
                ('movimentos_fasciculacoes', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Fasciculações')),
                ('movimentos_outros', models.TextField(blank=True, verbose_name='Outros')),
                ('coordenacao_decomposicao', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Decomposição de Movimento')),
                ('coordenacao_dismetria', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Dismetria')),
                ('coordenacao_rechaco', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Rechaço de Stewart-Holmes')),
                ('coordenacao_ataxia', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Ataxia Crebelar')),
                ('coordenacao_nistagmo', models.CharField(blank=True, choices=[(None, '----'), ('Não', 'Não'), ('Sim', 'Sim')], max_length=40, verbose_name='Nistagmo')),
                ('equilibrio', models.TextField(blank=True, verbose_name='Equilíbrio')),
                ('escala_grau', models.CharField(blank=True, choices=[('Grau 1', 'Grau 1: Tônus normal.'), ('Grau 2', 'Grau 2: Aumento leve do tônus - movimentação passiva com certa resistência.'), ('Grau 3', 'Grau 3: Aumento moderado do tônus - maior resistência à movimentação passiva.'), ('Grau 4', 'Grau 4: Aumento considerável do tônus - movimentação passiva é difícil.'), ('Grau 5', 'Grau 5: Rigidez em flexão ou extensão.')], max_length=40, verbose_name='Tônus Asworth')),
                ('escala_perimetria', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Alterada', 'Alterada'), ('Discrepância', 'Discrepância')], max_length=40, verbose_name='Perimetria')),
                ('escala_trofismo', models.CharField(blank=True, choices=[('Normo', 'Normo'), ('Hipertrofia', 'Hipertrofia'), ('Hipotrofia', 'Hipotrofia')], max_length=40, verbose_name='Trofismo')),
                ('mmss', models.CharField(blank=True, max_length=40, verbose_name='MMSS')),
                ('mmss_direito_7', models.CharField(blank=True, max_length=40, verbose_name='Direito - 7cm')),
                ('mmss_direito_14', models.CharField(blank=True, max_length=40, verbose_name='Direito - 14cm')),
                ('mmss_direito_21', models.CharField(blank=True, max_length=40, verbose_name='Direito - 21cm')),
                ('mmss_esquerdo_7', models.CharField(blank=True, max_length=40, verbose_name='Esquerdo - 7cm')),
                ('mmss_esquerdo_14', models.CharField(blank=True, max_length=40, verbose_name='Esquerdo - 14cm')),
                ('mmss_esquerdo_21', models.CharField(blank=True, max_length=40, verbose_name='Esquerdo - 21cm')),
                ('mmii', models.CharField(blank=True, max_length=40, verbose_name='MMII')),
                ('mmii_direito_7', models.CharField(blank=True, max_length=40, verbose_name='Direito - 7cm')),
                ('mmii_direito_14', models.CharField(blank=True, max_length=40, verbose_name='Direito - 14cm')),
                ('mmii_direito_21', models.CharField(blank=True, max_length=40, verbose_name='Direito - 21cm')),
                ('mmii_esquerdo_7', models.CharField(blank=True, max_length=40, verbose_name='Esquerdo - 7cm')),
                ('mmii_esquerdo_14', models.CharField(blank=True, max_length=40, verbose_name='Esquerdo - 14cm')),
                ('mmii_esquerdo_21', models.CharField(blank=True, max_length=40, verbose_name='Esquerdo - 21cm')),
                ('reflexos_bicipital', models.CharField(blank=True, choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], max_length=40, verbose_name='Bicipital - C6')),
                ('reflexos_tricipital', models.CharField(blank=True, choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], max_length=40, verbose_name='Tricipital - C7')),
                ('reflexos_patelar', models.CharField(blank=True, choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], max_length=40, verbose_name='Patelar - L2, L3 e L4')),
                ('reflexos_anquileu', models.CharField(blank=True, choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], max_length=40, verbose_name='Anquileu - L5, S1 e S2')),
                ('sensibilidade_superficial', models.CharField(blank=True, max_length=40, verbose_name='Sensibilidade Superficial (Exterioceptiva)')),
                ('sensibilidade_tatil', models.CharField(blank=True, choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], max_length=40, verbose_name='Tátil')),
                ('sensibilidade_termica', models.CharField(blank=True, choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], max_length=40, verbose_name='Térmica e Dolorosa')),
                ('sensibilidade_profunda', models.CharField(blank=True, max_length=40, verbose_name='Sensibilidade Profunda')),
                ('sensibilidade_cinetica', models.CharField(blank=True, choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], max_length=40, verbose_name='Cinética - Postural')),
                ('sensibilidade_combinada', models.CharField(blank=True, max_length=40, verbose_name='Sensibilidade Combinada')),
                ('sensibilidade_topognosia', models.CharField(blank=True, choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], max_length=40, verbose_name='Topognosia')),
                ('sensibilidade_esterognosia', models.CharField(blank=True, choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], max_length=40, verbose_name='Esterognosia')),
                ('sensibilidade_barognosia', models.CharField(blank=True, choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], max_length=40, verbose_name='Barognosia')),
                ('ms_direito_ombro', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Ombro')),
                ('ms_direito_cotovelo', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Cotovelo')),
                ('ms_direito_punho', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Punho')),
                ('ms_direito_mao', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Mão')),
                ('ms_direito_dedos', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Dedos')),
                ('ms_esquerdo_ombro', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Ombro')),
                ('ms_esquerdo_cotovelo', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Cotovelo')),
                ('ms_esquerdo_punho', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Punho')),
                ('ms_esquerdo_mao', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Mão')),
                ('ms_esquerdo_dedos', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Dedos')),
                ('mi_direito_quadril', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Quadril')),
                ('mi_direito_joelho', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Joelho')),
                ('mi_direito_tornozelo', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Tornozelo')),
                ('mi_direito_pe', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Pé')),
                ('mi_esquerdo_quadril', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Quadril')),
                ('mi_esquerdo_joelho', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Joelho')),
                ('mi_esquerdo_tornozelo', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Tornozelo')),
                ('mi_esquerdo_pe', models.CharField(blank=True, choices=[('N', 'Normal'), ('R', 'Reduzida')], max_length=40, verbose_name='Pé')),
                ('desenvolvimento_avds', models.CharField(blank=True, choices=[('Independente', 'Independente'), ('Dependente', 'Dependente'), ('Semi-Independente', 'Semi-Independente')], max_length=40, verbose_name="AVD's")),
                ('desenvolvimento_neurofuncional', models.TextField(blank=True, verbose_name='NeuroFuncional')),
                ('objetivos_tratamento', models.TextField(blank=True, verbose_name='Tratamento')),
                ('objetivos_conduta', models.TextField(blank=True, verbose_name='Conduta Fisioterapêutica')),
                ('atendimento_estagiario', models.CharField(blank=True, max_length=40, verbose_name='Estagiário (a)')),
                ('atendimento_supervisor', models.CharField(blank=True, max_length=40, verbose_name='Supervissor (a)')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente', verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Avaliações Acidente Vascular Encefálico',
                'verbose_name': 'Avaliação Acidente Vascular Encefálico',
                'ordering': ['data'],
            },
        ),
    ]