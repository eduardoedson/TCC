from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from servicos.models import AreaAtendimento, Disciplina, Setor
from utils import (CONTRACAO, ESCALA_FUNCIONAL_BERG, RANGE_SEXO, SINSINESIAS,
                   TONUS, YES_NO_CHOICES)


def media_path(instance, filename):
    dir = _('./prontuario/%(nome)s/%(especialidade)s/%(data)s/%(arq)s') % {
        'nome' : instance.paciente.nome,
        'especialidade' : instance.especialidade,
        'data' : instance.data.strftime('%d-%m-%Y'),
        'arq' : filename
    }
    return zdir

class Recepcionista(models.Model):
    nome = models.CharField(max_length=80, verbose_name=_('Nome Completo'))
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    setor = models.ForeignKey(Setor, verbose_name=_('Setor Responsável'))

    # Dados para logar no sistema
    user = models.ForeignKey(User)
    email = email = models.EmailField(unique=True, verbose_name=_('Email'), blank=True)
    username = models.CharField(verbose_name=_('Nome de Usuário'), unique=True, max_length=30)

    class Meta:
        verbose_name = _('Recepcionista')
        verbose_name_plural = _('Recepcionistas')
        ordering = ['nome', 'setor']

    def __str__(self):
        return _('%(nome)s (%(setor)s)') % {
            'nome': self.nome, 'setor': self.setor.descricao}


class Supervisor(models.Model):
    nome = models.CharField(max_length=80, verbose_name=_('Nome Completo'))
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    setor = models.ForeignKey(Setor, verbose_name=_('Setor Responsável'))
    matricula = models.CharField(max_length=13, blank=True, null=True, verbose_name=_('Matrícula'))

    telefone = models.CharField(max_length=14, blank=True, null=True, verbose_name=_('Telefone'))
    celular = models.CharField(max_length=15, verbose_name=_('Celular'), blank=True)

    # Dados para logar no sistema
    user = models.ForeignKey(User)
    email = email = models.EmailField(unique=True, verbose_name=_('Email'), blank=True)
    username = models.CharField(verbose_name=_('Nome de Usuário'), unique=True, max_length=30)

    class Meta:
        verbose_name = _('Supervisor (a)')
        verbose_name_plural = _('Supervisores (as)')
        ordering = ['nome', 'setor']

    def __str__(self):
        return _('%(nome)s (%(setor)s)') % {
            'nome': self.nome, 'setor': self.setor.descricao}


class Aluno(models.Model):
    nome = models.CharField(max_length=80, verbose_name=_('Nome Completo'))
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    disciplina = models.ForeignKey(Disciplina, verbose_name=_('Disciplina'))
    matricula = models.CharField(max_length=13, blank=True, null=True, verbose_name=_('Matrícula'))

    telefone = models.CharField(max_length=14, blank=True, null=True, verbose_name=_('Telefone'))
    celular = models.CharField(max_length=15, verbose_name=_('Celular'))

    # Dados para logar no sistema
    user = models.ForeignKey(User)
    email = email = models.EmailField(unique=True, verbose_name=_('Email'))
    username = models.CharField(verbose_name=_('Nome de Usuário'), unique=True, max_length=30)

    supervisor = models.ForeignKey(Supervisor, verbose_name=_('Supervisor'))

    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=80, verbose_name=_('Nome Completo'))
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'))
    rg = models.CharField(max_length=9, verbose_name=_('RG'))
    cpf = models.CharField(max_length=14, verbose_name=_('CPF'))
    profissao = models.CharField(max_length=14, verbose_name=_('Profissão'), blank=True)
    renda = models.CharField(max_length=14, verbose_name=_('Renda Mensal'), blank=True)
    convenio = models.CharField(max_length=14, verbose_name=_('Convênio Médico'), blank=True)

    grupo_familiar = models.CharField(max_length=3, verbose_name=_('Mora com quantas pessoas?'), blank=True)
    renda_total = models.CharField(max_length=14, verbose_name=_('Renda Total da Família'), blank=True)

    telefone = models.CharField(max_length=14, blank=True, null=True, verbose_name=_('Telefone'))
    celular = models.CharField(max_length=15, verbose_name=_('Celular'))

    cep = models.CharField(max_length=10, verbose_name=_('CEP'))
    endereco = models.CharField(max_length=50, verbose_name=_('Endereço'), blank=True)
    numero = models.CharField(max_length=5, verbose_name=_('Número'), blank=True)
    complemento = models.CharField(max_length=50, verbose_name=_('Complemento'), blank=True)
    bairro = models.CharField(max_length=30, verbose_name=_('Bairro'), blank=True)
    referencia = models.CharField(max_length=30, verbose_name=_('Ponto de Referência'), blank=True)
    uf = models.CharField(max_length=2, verbose_name=_('UF'), blank=True)

    data_cadastro = models.DateField(auto_now_add=True)

    colaborador = models.CharField(
        max_length=10,
        verbose_name=_('Colaborador da instituição?'),
        choices=YES_NO_CHOICES,
        default='Não')

    moradia = models.CharField(max_length=30, verbose_name=_('Condição da Moradia'), blank=True)
    valor_aluguel = models.CharField(max_length=30, verbose_name=_('Se alugada, Valor'), blank=True)

    tratamento_sus = models.CharField(
        max_length=10,
        verbose_name=_('Realiza tratamento pelo SUS?'),
        choices=YES_NO_CHOICES)

    beneficio = models.CharField(
        max_length=10,
        verbose_name=_('Possui beneficio do governo?'),
        choices=YES_NO_CHOICES)

    referencia_nome = models.CharField(max_length=80, verbose_name=_('Nome'), blank=True)
    referencia_telefone = models.CharField(max_length=15, verbose_name=_('Telefone'), blank=True)
    referencia_parentesco = models.CharField(max_length=80, verbose_name=_('Parentesco'), blank=True)

    class Meta:
        verbose_name = _('Paciente')
        verbose_name_plural = _('Pacientes')
        ordering = ['nome', 'data_cadastro']

    def __str__(self):
        return self.nome


class FisioterapiaTriagem(models.Model):
    data_triagem = models.DateField(auto_now_add=True, verbose_name=_('Data Triagem'), blank=True)
    data_laudo = models.DateField(verbose_name=_('Data Laudo Médico'), blank=True)

    area_atendimento = models.ForeignKey(AreaAtendimento, verbose_name=_('Área de Atendimento'), blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=_('Paciente'), blank=True)

    avds_independente = models.CharField(max_length=30, verbose_name=_('AVD\'S Independente'), blank=True)
    tempo_lesao = models.CharField(max_length=30, verbose_name=_('Tempo de Lesão'), blank=True)
    marcha_independente = models.CharField(max_length=30, verbose_name=_('Marcha Independente'), blank=True)
    cid = models.CharField(max_length=30, verbose_name=_('CID'), blank=True)

    uso_medicamentos = models.CharField(
        max_length=10,
        verbose_name=_('Faz uso de medicamentos?'),
        choices=YES_NO_CHOICES, default='Não')
    atividade_fisica = models.CharField(
        max_length=10,
        verbose_name=_('Pratica atividade física?'),
        choices=YES_NO_CHOICES, default='Não')
    atividade_laboral = models.CharField(
        max_length=10,
        verbose_name=_('Pratica atividade laboral?'),
        choices=YES_NO_CHOICES, default='Não')

    relato = models.TextField(verbose_name=_('Relato do Paciente'), blank=True)
    diagnostico = models.TextField(verbose_name=_('Diagnóstico Clínico'), blank=True)
    queixa_principal = models.TextField(verbose_name=_('Queixa Principal'), blank=True)
    patologia = models.TextField(verbose_name=_('Patologias Associadas'), blank=True)
    tratamento_anterior = models.TextField(verbose_name=_('Tratamento Anterior'), blank=True)
    exames_complementares = models.TextField(verbose_name=_('Exames Complementares'), blank=True)
    parecer = models.TextField(verbose_name=_('Parecer para atendimento'), blank=True)

    class Meta:
        verbose_name = _('Triagem de Fisioterapia')
        verbose_name_plural = _('Triagens de Fisioterapia ')
        ordering = ['data_triagem']

    def __str__(self):
        return _('%(area)s (%(data)s)') % {
            'area': self.area_atendimento, 'data': self.data_triagem.strftime('%d/%m/%Y')}

class FisioterapiaEvolucao(models.Model):
    data = models.DateField(verbose_name=_('Data'))
    paciente = models.ForeignKey(Paciente, verbose_name=_('Paciente'))
    descricao = models.TextField(verbose_name=_('Descrição'))

    class Meta:
        verbose_name = _('Evolução')
        verbose_name_plural = _('Evoluções')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {
            'data': self.data.strftime('%d/%m/%Y')}

class FisioterapiaNeurologiaInfantilAvalicao(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data = models.DateField(verbose_name=_('Data'), blank=True)

    responsavel = models.CharField(max_length=50, verbose_name=_('Responsável'), blank=True)
    idade = models.CharField(max_length=50, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO, blank=True)
    endereco = models.CharField(max_length=50, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=15, verbose_name=_('Telefone'), blank=True)
    medico = models.CharField(max_length=50, verbose_name=_('Médico Responsável'), blank=True)

    diagnostico = models.TextField(verbose_name=_('Diagnóstico Clínico'), blank=True)

    historio_comprimento = models.CharField(max_length=50, verbose_name=_('Comprimento'), blank=True)
    historio_peso = models.CharField(max_length=50, verbose_name=_('Peso'), blank=True)
    historio_pc = models.CharField(max_length=50, verbose_name=_('P.C.'), blank=True)
    historio_apgar = models.CharField(max_length=50, verbose_name=_('Apgar'), blank=True)

    anamnese_fisioterapia = models.CharField(max_length=20, verbose_name=_('Realiza fisioterapia?'), choices=YES_NO_CHOICES, blank=True)
    anamnese_constipacao = models.CharField(max_length=20, verbose_name=_('Constipação'), choices=YES_NO_CHOICES, blank=True)
    anamnese_sialorreia = models.CharField(max_length=20, verbose_name=_('Sialorréia'), choices=YES_NO_CHOICES, blank=True)
    anamnese_refluxo = models.CharField(max_length=20, verbose_name=_('Refluxo'), choices=YES_NO_CHOICES, blank=True)
    anamnese_atitude = models.CharField(max_length=20, verbose_name=_('Atitude'), choices=[('Passiva', _('Passiva')), ('Hipoativa', _('Hipoativa')), ('Ativa', _('Ativa'))], blank=True)
    anamnese_visao = models.CharField(max_length=20, verbose_name=_('Visão'), choices=[('Sem alteração', _('Sem alteração')), ('Deficiência', _('Deficiência'))], blank=True)
    anamnese_avd = models.CharField(max_length=20, verbose_name=_('AVD'), choices=[('Sem alteração', _('Sem alteração')), ('Deficiência', _('Deficiência'))], blank=True)

    anamnese_escola = models.CharField(max_length=20, verbose_name=_('Frequenta Escola?'), choices=YES_NO_CHOICES, blank=True)
    anamnese_escola_motivo = models.CharField(max_length=50, verbose_name=_('Frequenta Escola? Justificativa'), blank=True)
    anamnese_convulsao = models.CharField(max_length=20, verbose_name=_('Convulsões?'), choices=YES_NO_CHOICES, blank=True)
    anamnese_convulsao_motivo = models.CharField(max_length=50, verbose_name=_('Convulsões? Frequência'), blank=True)
    anamnese_dor = models.CharField(max_length=20, verbose_name=_('Dor?'), choices=YES_NO_CHOICES, blank=True)
    anamnese_dor_motivo = models.CharField(max_length=50, verbose_name=_('Quais dores?'), blank=True)
    anamnese_cirurgia = models.CharField(max_length=20, verbose_name=_('Interveções Cirúrgica?'), choices=YES_NO_CHOICES, blank=True)
    anamnese_cirurgia_motivo = models.CharField(max_length=50, verbose_name=_('Quais cirúrgias?'), blank=True)

    anamnese_comunicacao = models.CharField(max_length=50, verbose_name=_('Comunicação'), blank=True)

    anamnese_medicamentos = models.TextField(verbose_name=_('Medicamentos'), blank=True)

    queixa_principal = models.TextField(verbose_name=_('Queixa Principal'), blank=True)

    exame_pele = models.CharField(max_length=10, verbose_name=_('Pele'), blank=True)
    exame_edema = models.CharField(max_length=10, verbose_name=_('Edema'), blank=True)
    exame_cicatrizes = models.CharField(max_length=10, verbose_name=_('Cicatrizes'), blank=True)
    exame_tonus = models.CharField(max_length=10, verbose_name=_('Tônus/Trofismo Muscular'), blank=True)
    exame_reflexos = models.CharField(max_length=10, verbose_name=_('Reflexos'), blank=True)
    exame_deformidades = models.CharField(max_length=10, verbose_name=_('Deformidades'), blank=True)
    exame_complementares = models.CharField(max_length=10, verbose_name=_('Exames Complementares'), blank=True)
    exame_observacao = models.CharField(max_length=10, verbose_name=_('Observações Importantes'), blank=True)

    exame_aquisicao_motora = models.TextField(verbose_name=_('Aquisições Motoras'), blank=True)
    exame_diagnostico = models.TextField(verbose_name=_('Diagnóstico Fisioterapêutico'), blank=True)
    exame_proposta = models.TextField(verbose_name=_('Proposta Fisioterapêutico'), blank=True)

    class Meta:
        verbose_name = _('Avaliação Fisioterápica em Neuropediatria')
        verbose_name_plural = _('Avaliações Fisioterápica em Neuropediatria')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s %(responsavel)s') % {
            'data': self.data.strftime('%d/%m/%Y'), 'responsavel': self.responsavel}


class FisioterapiaGeriatriaAvalicao(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    idade = models.CharField(max_length=50, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO, blank=True)
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    data_admissao = models.DateField(verbose_name=_('Data da Admissão'), blank=True)
    data_avaliacao = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)

    diagnostico_clinico = models.TextField(verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapeutico = models.TextField(verbose_name=_('Diagnóstico Fisioterapêutico'), blank=True)
    patologia = models.TextField(verbose_name=_('Patologias/Problemas Associados'), blank=True)

    medicamento = models.CharField(max_length=20, verbose_name=_('Faz uso de medicamentos?'), choices=YES_NO_CHOICES, default='Não')
    medicamentos = models.TextField(verbose_name=_('Quais medicamentos?'), blank=True)

    anamnese_queixa = models.TextField(verbose_name=_('Queixa Principal/HMA'), blank=True)
    anamnese_historia = models.TextField(verbose_name=_('História Pregressa'), blank=True)

    exame_pressao = models.CharField(max_length=20, verbose_name=_('Pressão Arterial (mmHg)'), blank=True)
    exame_freq_cardiaca = models.CharField(max_length=20, verbose_name=_('Frequência Cardíaca (bpm)'), blank=True)
    exame_freq_respiratoria = models.CharField(max_length=20, verbose_name=_('Frequência Respiratória (irpm)'), blank=True)
    exame_inspecao = models.CharField(max_length=20, verbose_name=_('Inspeção'), blank=True)
    exame_postura = models.CharField(max_length=20, verbose_name=_('Postura'), blank=True)
    exame_palpacao = models.CharField(max_length=20, verbose_name=_('Palpação/Dor'), blank=True)
    exame_trofismo = models.CharField(max_length=20, verbose_name=_('Trofismo'), blank=True)
    exame_tonus = models.CharField(max_length=20, verbose_name=_('Tônus'), blank=True)
    exame_sensibilidade = models.CharField(max_length=20, verbose_name=_('Sensibilidade'), blank=True)

    amplitude_superiores = models.CharField(max_length=20, verbose_name=_('Membros Superiores'), blank=True)
    amplitude_inferiores = models.CharField(max_length=20, verbose_name=_('Membros Inferiores'), blank=True)
    amplitude_tronco = models.CharField(max_length=20, verbose_name=_('Tronco'), blank=True)

    forca_superiores = models.CharField(max_length=20, verbose_name=_('Membros Superiores'), blank=True)
    forca_inferiores = models.CharField(max_length=20, verbose_name=_('Membros Inferiores'), blank=True)
    forca_tronco = models.CharField(max_length=20, verbose_name=_('Tronco'), blank=True)
    forca_retracao = models.CharField(max_length=20, verbose_name=_('Retrações/Encurtamentos'), blank=True)
    forca_equilibrio = models.CharField(max_length=20, verbose_name=_('Equilíbrio'), blank=True)
    forca_marcha = models.CharField(max_length=20, verbose_name=_('Marcha'), blank=True)
    forca_obs = models.TextField(verbose_name=_('Obs.'), blank=True)

    atividade_alimentacao = models.CharField(max_length=20, verbose_name=_('Alimentação'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_mobilidade = models.CharField(max_length=20, verbose_name=_('Mobilidade'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10')), ('15', _('15'))], default='00')
    atividade_cuidado = models.CharField(max_length=20, verbose_name=_('Cuidado Pessoal'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_banheiro = models.CharField(max_length=20, verbose_name=_('Uso do Banheiro'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_banho = models.CharField(max_length=20, verbose_name=_('Banho'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_vestir = models.CharField(max_length=20, verbose_name=_('Vestir-se'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_transferencia = models.CharField(max_length=20, verbose_name=_('Tranferência'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10')), ('15', _('15'))], default='00')
    atividade_escada = models.CharField(max_length=20, verbose_name=_('Escada'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_fecal = models.CharField(max_length=20, verbose_name=_('Controle Fecal'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_urinario = models.CharField(max_length=20, verbose_name=_('Controle Urinário'), choices=[('00', _('00')), ('05', _('05')), ('10', _('10'))], default='00')
    atividade_total = models.CharField(max_length=30, verbose_name=_('Total de Pontos'), blank=True)

    planejamento_objetivos = models.TextField(verbose_name=_('Objetivos'), blank=True)
    planejamento_tratamento = models.TextField(verbose_name=_('Tratamento'), blank=True)

    estagiario = models.ForeignKey(Aluno, verbose_name=_('Estagiário'))
    supervisor = models.ForeignKey(Supervisor, verbose_name=_('Supervisor'))

    class Meta:
        verbose_name = _('Avaliação de Geriatria')
        verbose_name_plural = _('Avaliações de Geriatria')
        ordering = ['data_avaliacao']

    def __str__(self):
        return _('%(data)s - %(estagiario)s') % {
            'data': self.data_avaliacao.strftime('%d/%m/%Y'),
            'estagiario': self.estagiario}

class FisioterapiaBerg(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data = models.DateField(verbose_name=_('Data'), blank=True)
    local = models.CharField(max_length=20, verbose_name=_('Local'), blank=True)
    avaliador = models.CharField(max_length=20, verbose_name=_('Avaliador'), blank=True)

    berg_1 = models.CharField(
        max_length=10,
        verbose_name=_('1. Posição sentada para posição em pé: '),
        default=0)

    berg_2 = models.CharField(
        max_length=10,
        verbose_name=_('2. Permanecer em pé sem apoio: '),
        default=0)

    berg_3 = models.CharField(
        max_length=10,
        verbose_name=_('3. Permanecer sentado sem apoio nas costas, mas com os pés apoiados no chão ou num banquinho: '),
        default=0)

    berg_4 = models.CharField(
        max_length=10,
        verbose_name=_('4. Posição em pé para posição sentada: '),
        default=0)

    berg_5 = models.CharField(
        max_length=10,
        verbose_name=_('5. Transferências: '),
        default=0)

    berg_6 = models.CharField(
        max_length=10,
        verbose_name=_('6. Permanecer em pé sem apoio com os olhos fechados: '),
        default=0)

    berg_7 = models.CharField(
        max_length=10,
        verbose_name=_('7. Permanecer em pé sem apoio com os pés juntos: '),
        default=0)

    berg_8 = models.CharField(
        max_length=10,
        verbose_name=_('8. Alcançar a frente com o braço estendido permanecendo em pé: '),
        default=0)

    berg_9 = models.CharField(
        max_length=10,
        verbose_name=_('9. Pegar um objeto do chão a partir de uma posição em pé: '),
        default=0)

    berg_10 = models.CharField(
        max_length=10,
        verbose_name=_('10. Virar-se e olhar para trás por cima dos ombros direito e esquerdo enquanto permanece em pé: '),
        default=0)

    berg_11 = models.CharField(
        max_length=10,
        verbose_name=_('11. Girar-se 360 graus: '),
        default=0)

    berg_12 = models.CharField(
        max_length=10,
        verbose_name=_('12. Posicionar os pés alternadamente no degrau ou banquinho enquanto permanece em pé sem apoio: '),
        default=0)

    berg_13 = models.CharField(
        max_length=10,
        verbose_name=_('13. Permanecer em pé sem apoio com um pé à frente: '),
        default=0)

    berg_14 = models.CharField(
        max_length=10,
        verbose_name=_('14. Permanecer em pé sobre uma perna: '),
        default=0)

    berg_total = models.CharField(max_length=20, verbose_name=_('Escore Total (Máximo = 56)'), blank=True)

    class Meta:
        verbose_name = _('Escala de Equilíbrio Funcional de Berg')
        verbose_name_plural = _('Escala de Equilíbrio Funcional de Berg')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s - %(total)s') % {
            'data': self.data.strftime('%d/%m/%Y'),
            'total': self.berg_total}


class FisioterapiaGeriatriaAnamnese(models.Model):
    data = models.DateField(verbose_name=_('Data'), blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO, blank=True)
    estado_civil = models.CharField(max_length=20, verbose_name=_('Estado Civil'), blank=True, choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viúvo', 'Viúvo')])
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=20, verbose_name=_('Idade'), blank=True)
    membro_dominante = models.CharField(max_length=20, verbose_name=_('Membro Dominante'), blank=True, choices=[('Direito', 'Direito'), ('Esquerdo', 'Esquerdo')])
    trabalha = models.CharField(max_length=10, verbose_name=_('Trabalha?'), choices=YES_NO_CHOICES, default='Não')
    funcao = models.CharField(max_length=40, verbose_name=_('Função'), blank=True)
    tempo_trabalho = models.CharField(max_length=40, verbose_name=_('Tempo de Trabalho'), blank=True)
    ocupacao = models.CharField(max_length=20, verbose_name=_('Ocupação Atual'), blank=True, choices=[('Aposentado', 'Aposentado'), ('Pensionista', 'Pensionista'), ('Autônomo', 'Autônomo'), ('Voluntário', 'Voluntário')])
    aviso = models.CharField(max_length=40, verbose_name=_('Em caso de Aviso Ligar p/'), blank=True)
    emergencia = models.CharField(max_length=40, verbose_name=_('Em caso de Emergência Ligar p/'), blank=True)

    peso = models.CharField(max_length=40, verbose_name=_('Peso'), blank=True)
    altura = models.CharField(max_length=40, verbose_name=_('Altura'), blank=True)
    imc = models.CharField(max_length=40, verbose_name=_('IMC'), blank=True)

    pa = models.CharField(max_length=40, verbose_name=_('PA'), blank=True)
    fc = models.CharField(max_length=40, verbose_name=_('FC'), blank=True)
    fr = models.CharField(max_length=40, verbose_name=_('FR'), blank=True)
    saturacao = models.CharField(max_length=40, verbose_name=_('Saturação'), blank=True)

    diabetes = models.CharField(max_length=10, verbose_name=_('Diabetes?'), choices=YES_NO_CHOICES, default='Não')
    diabetes_tipo = models.CharField(max_length=40, verbose_name=_('Tipo?'), blank=True)
    diabetes_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    hipertiroidismo = models.CharField(max_length=10, verbose_name=_('Hipertiroidismo?'), choices=YES_NO_CHOICES, default='Não')
    hipertiroidismo_tipo = models.CharField(max_length=40, verbose_name=_('Tipo?'), blank=True)
    hipertiroidismo_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    hipotiroidismo = models.CharField(max_length=10, verbose_name=_('Hipotiroidismo?'), choices=YES_NO_CHOICES, default='Não')
    hipotiroidismo_tipo = models.CharField(max_length=40, verbose_name=_('Tipo'), blank=True)
    hipotiroidismo_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    obesidade = models.CharField(max_length=10, verbose_name=_('Obesidade?'), choices=YES_NO_CHOICES, default='Não')
    obesidade_tipo = models.CharField(max_length=40, verbose_name=_('Tipo?'), blank=True)
    obesidade_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    outras_metabolicas = models.CharField(max_length=10, verbose_name=_('Outras?'), choices=YES_NO_CHOICES, default='Não')
    outras_metabolicas_quais = models.TextField(verbose_name=_('Quais?'), blank=True)

    infarto = models.CharField(max_length=10, verbose_name=_('Infarto Agudo do Miocárdio?'), choices=YES_NO_CHOICES, default='Não')
    infarto_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    hipertensao = models.CharField(max_length=10, verbose_name=_('Hipertensão?'), choices=YES_NO_CHOICES, default='Não')
    hipertensao_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    hipotensao = models.CharField(max_length=10, verbose_name=_('Hipotensão?'), choices=YES_NO_CHOICES, default='Não')
    hipotensao_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    vaso_vagal = models.CharField(max_length=10, verbose_name=_('Síndrome do Vaso Vagal?'), choices=YES_NO_CHOICES, default='Não')
    vaso_vagal_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    chagas = models.CharField(max_length=10, verbose_name=_('Chagas?'), choices=YES_NO_CHOICES, default='Não')
    chagas_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    outras_cardiovasculares = models.CharField(max_length=10, verbose_name=_('Outras?'), choices=YES_NO_CHOICES, default='Não')
    outras_cardiovasculares_quais = models.TextField(verbose_name=_('Quais?'), blank=True)

    bronquite = models.CharField(max_length=10, verbose_name=_('Bronquite Crônica?'), choices=YES_NO_CHOICES, default='Não')
    bronquite_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    enfisema = models.CharField(max_length=10, verbose_name=_('Enfisema Pulmonar?'), choices=YES_NO_CHOICES, default='Não')
    enfisema_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    asma = models.CharField(max_length=10, verbose_name=_('Asma Brônquica?'), choices=YES_NO_CHOICES, default='Não')
    asma_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    bronquiectasias = models.CharField(max_length=10, verbose_name=_('Bronquiectasias?'), choices=YES_NO_CHOICES, default='Não')
    bronquiectasias_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    apneia = models.CharField(max_length=10, verbose_name=_('Apnéia?'), choices=YES_NO_CHOICES, default='Não')
    apneia_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    alergia = models.CharField(max_length=10, verbose_name=_('Alergias?'), choices=YES_NO_CHOICES, default='Não')
    alergia_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    outras_respiratorias = models.CharField(max_length=10, verbose_name=_('Outras?'), choices=YES_NO_CHOICES, default='Não')
    outras_respiratorias_quais = models.TextField(verbose_name=_('Quais?'), blank=True)

    stress = models.CharField(max_length=10, verbose_name=_('Stress?'), choices=YES_NO_CHOICES, default='Não')
    stress_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    depressao = models.CharField(max_length=10, verbose_name=_('Depressão?'), choices=YES_NO_CHOICES, default='Não')
    depressao_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    fibromialgia = models.CharField(max_length=10, verbose_name=_('Fibromialgia?'), choices=YES_NO_CHOICES, default='Não')
    fibromialgia_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    outras_psicossomaticas = models.CharField(max_length=10, verbose_name=_('Outras?'), choices=YES_NO_CHOICES, default='Não')
    outras_psicossomaticas_quais = models.TextField(verbose_name=_('Quais?'), blank=True)

    labirintite = models.CharField(max_length=10, verbose_name=_('Labirintite?'), choices=YES_NO_CHOICES, default='Não')
    labirintite_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    avc = models.CharField(max_length=10, verbose_name=_('AVC (Derrame Cerebral)?'), choices=YES_NO_CHOICES, default='Não')
    avc_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    traumatismo = models.CharField(max_length=10, verbose_name=_('Traumatismo Cranioencefálico?'), choices=YES_NO_CHOICES, default='Não')
    traumatismo_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    hernia = models.CharField(max_length=10, verbose_name=_('Hérnia de Disco?'), choices=YES_NO_CHOICES, default='Não')
    hernia_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    incontinencia = models.CharField(max_length=10, verbose_name=_('Incontinênia Urinária?'), choices=YES_NO_CHOICES, default='Não')
    incontinencia_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    alzheimer = models.CharField(max_length=10, verbose_name=_('Alzheimer?'), choices=YES_NO_CHOICES, default='Não')
    alzheimer_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    outras_neurologicas = models.CharField(max_length=10, verbose_name=_('Outras?'), choices=YES_NO_CHOICES, default='Não')
    outras_neurologicas_quais = models.TextField(verbose_name=_('Quais?'), blank=True)

    osteoporose = models.CharField(max_length=10, verbose_name=_('Osteoporose?'), choices=YES_NO_CHOICES, default='Não')
    osteoporose_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    osteoporose_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    artrite = models.CharField(max_length=10, verbose_name=_('Artrite/Artrose?'), choices=YES_NO_CHOICES, default='Não')
    artrite_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    artrite_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    lombalgia = models.CharField(max_length=10, verbose_name=_('Lombalgia?'), choices=YES_NO_CHOICES, default='Não')
    lombalgia_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    lombalgia_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    bursite = models.CharField(max_length=10, verbose_name=_('Bursite?'), choices=YES_NO_CHOICES, default='Não')
    bursite_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    bursite_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    tendinite = models.CharField(max_length=10, verbose_name=_('Tendinite?'), choices=YES_NO_CHOICES, default='Não')
    tendinite_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    tendinite_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    fratura = models.CharField(max_length=10, verbose_name=_('Fratura?'), choices=YES_NO_CHOICES, default='Não')
    fratura_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    fratura_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    carpo = models.CharField(max_length=10, verbose_name=_('Síndrome do Túnel do Carpo?'), choices=YES_NO_CHOICES, default='Não')
    carpo_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    carpo_tempo = models.CharField(max_length=40, verbose_name=_('Quanto Tempo?'), blank=True)
    outras_osteomioarticulares = models.CharField(max_length=10, verbose_name=_('Outras?'), choices=YES_NO_CHOICES, default='Não')
    outras_osteomioarticulares_quais = models.TextField(verbose_name=_('Quais?'), blank=True)

    medicamento = models.CharField(max_length=20, verbose_name=_('Faz uso de medicamentos?'), choices=YES_NO_CHOICES, default='Não')
    medicamentos = models.TextField(verbose_name=_('Quais medicamentos?'), blank=True)

    fumante = models.CharField(max_length=10, verbose_name=_('Fumante?'), choices=YES_NO_CHOICES, default='Não')
    fumante_tempo = models.CharField(max_length=40, verbose_name=_('Há Quanto Tempo?'), blank=True)
    fumante_qnd_parou = models.CharField(max_length=40, verbose_name=_('Quando Parou?'), blank=True)
    queda = models.CharField(max_length=10, verbose_name=_('Sofreu quedas no último ano?'), choices=YES_NO_CHOICES, default='Não')
    cirurgia = models.CharField(max_length=10, verbose_name=_('Realizou cirurgia nos últimos 5 anos?'), choices=YES_NO_CHOICES, default='Não')
    cirurgia_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)
    atividade_fisica = models.CharField(max_length=10, verbose_name=_('Pratica Atividade Física?'), choices=YES_NO_CHOICES, default='Não')
    atividade_fisica_qual = models.CharField(max_length=40, verbose_name=_('Qual?'), blank=True)
    atividade_fisica_frequencia = models.CharField(max_length=40, verbose_name=_('Frequência?'), blank=True)

    cuidar_casa = models.CharField(max_length=10, verbose_name=_('Cuidar da Casa?'), choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não')
    lavar_roupa = models.CharField(max_length=10, verbose_name=_('Lavar Roupa?'), choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não')
    passar_roupa = models.CharField(max_length=10, verbose_name=_('Passar Roupa?'), choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não')
    jardinagem = models.CharField(max_length=10, verbose_name=_('Jardinagem?'), choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não')
    supermecado = models.CharField(max_length=10, verbose_name=_('Ir ao supermecado?'), choices=[('Não', 'Não'), ('1 a 2 vezes', '1 a 2 vezes'), ('3 a 4 vezes', '3 a 4 vezes'), ('5 a 6 vezes', '5 a 6 vezes')], default='Não')

    queda_2_anos = models.CharField(max_length=10, verbose_name=_('Nos 2 últimos anos o Sr(a) teve alguma queda?'), choices=YES_NO_CHOICES, default='Não')
    queda_como = models.CharField(max_length=40, verbose_name=_('Como foi?'), blank=True)
    queda_aonde = models.CharField(max_length=40, verbose_name=_('Aonde foi?'), blank=True)
    queda_hospital = models.CharField(max_length=10, verbose_name=_('Precisou ser hospitalizado?'), choices=YES_NO_CHOICES, default='Não')
    queda_hospital_tempo = models.CharField(max_length=40, verbose_name=_('Quanto tempo?'), blank=True)
    queda_cirurgia = models.CharField(max_length=10, verbose_name=_('Fez cirurgia?'), choices=YES_NO_CHOICES, default='Não')
    queda_cirurgia_qual = models.CharField(max_length=40, verbose_name=_('Qual?'), blank=True)
    queda_protese = models.CharField(max_length=10, verbose_name=_('Prótese?'), choices=YES_NO_CHOICES, default='Não')
    queda_protese_onde = models.CharField(max_length=40, verbose_name=_('Onde?'), blank=True)

    diagnostico = models.TextField(verbose_name=_('Diagnóstico Fisioterapêutico/Objetivos'), blank=True)
    conduta = models.TextField(verbose_name=_('Conduta'), blank=True)

    class Meta:
        verbose_name = _('Ficha de Avaliação / Anamnese')
        verbose_name_plural = _('Fichas de Avaliação / Anamnese')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaAvaliacaoGestacional(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    nome_pai = models.CharField(max_length=40, verbose_name=_('Nome do Pai da Criança'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    funcao = models.CharField(max_length=40, verbose_name=_('Função'), blank=True)
    endereco = models.CharField(max_length=100, verbose_name=_('Endereço'), blank=True)
    cep = models.CharField(max_length=40, verbose_name=_('CEP'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    nome_bebe = models.CharField(max_length=40, verbose_name=_('Nome do Bebê'), blank=True)
    sexo_bebe = models.CharField(max_length=1, verbose_name=_('Sexo do Bebê'), choices=RANGE_SEXO, blank=True)

    anamnese_queixa_principal = models.TextField(verbose_name=_('Queixa Principal'), blank=True)

    gestacional_tipo_sangue = models.CharField(max_length=1, verbose_name=_('Tipagem Sanguínea'), choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], default='A')
    gestacional_fator_rh = models.CharField(max_length=1, verbose_name=_('Fator RH'), choices=[('-', '-'), ('+', '+')], default='+')
    gestacional_dum = models.CharField(max_length=40, verbose_name=_('DUM'), blank=True)
    gestacional_dpp = models.CharField(max_length=40, verbose_name=_('DPP'), blank=True)
    gestacional_idade = models.CharField(max_length=40, verbose_name=_('Idade Gestacional'), blank=True)
    gestacional_data = models.CharField(max_length=40, verbose_name=_('Data dos Primeiros Movimentos Fetais'), blank=True)

    antecedentes_idade_menarca = models.CharField(max_length=40, verbose_name=_('Idade da Menarca (Anos)'), blank=True)
    antecedentes_idade_sexual = models.CharField(max_length=40, verbose_name=_('Idade de Início da Atiidade Sexual (Anos)'), blank=True)
    antecedentes_ciclo = models.CharField(max_length=40, verbose_name=_('Regularidade do Ciclo Menstrual'), choices=YES_NO_CHOICES, default='Sim')
    antecedentes_cirurgia = models.CharField(max_length=40, verbose_name=_('Cirurgia ou Doença Ginecológica Anterior'), choices=YES_NO_CHOICES, default='Não')
    antecedentes_cirurgia_qual = models.CharField(max_length=40, verbose_name=_('Qual?'), blank=True)

    obstetrica_gestacao = models.CharField(max_length=40, verbose_name=_('Número de Gestações Anteriores'), blank=True)
    obstetrica_parto = models.CharField(max_length=40, verbose_name=_('Tipo de Parto'), choices=[('Normal', 'Normal'), ('Cesárea', 'Cesárea'), ('Fórceps', 'Usou Fórceps')], default='Norma')
    obstetrica_complicacao = models.CharField(max_length=40, verbose_name=_('Complicações do Parto (Eclâmpsia e Pré-Eclâmpsia)'), blank=True)
    obstetrica_prematuridade = models.CharField(max_length=40, verbose_name=_('Prematuridade'), blank=True)
    obstetrica_abortos = models.CharField(max_length=40, verbose_name=_('Nº de Abortos'), blank=True)
    obstetrica_doencas = models.CharField(max_length=40, verbose_name=_('Doenças Associadas (DM? Hipertensão? IST?)'), blank=True)
    obstetrica_medicacao = models.CharField(max_length=40, verbose_name=_('Medicação'), blank=True)

    doenca_cardiopatias = models.CharField(max_length=40, verbose_name=_('Cardiopatias'), blank=True)
    doenca_hipertensao = models.CharField(max_length=40, verbose_name=_('Hipertensão'), blank=True)
    doenca_epilepsia = models.CharField(max_length=40, verbose_name=_('Epilepsia'), blank=True)
    doenca_neoplasias = models.CharField(max_length=40, verbose_name=_('Neoplasias'), blank=True)
    doenca_diabetes = models.CharField(max_length=40, verbose_name=_('Diabetes'), blank=True)
    doenca_psiquicas = models.CharField(max_length=40, verbose_name=_('Alterações Psíquicas'), blank=True)
    doenca_malformacao = models.CharField(max_length=40, verbose_name=_('Malformações'), blank=True)

    infecciosas_tuberculose = models.CharField(max_length=40, verbose_name=_('Tuberculose'), choices=YES_NO_CHOICES, default='Não')
    infecciosas_sifilis = models.CharField(max_length=40, verbose_name=_('Sífilis'), choices=YES_NO_CHOICES, default='Não')
    infecciosas_rubeola = models.CharField(max_length=40, verbose_name=_('Rubéola'), choices=YES_NO_CHOICES, default='Não')
    infecciosas_tuxoplasmose = models.CharField(max_length=40, verbose_name=_('Tuxoplasmose'), choices=YES_NO_CHOICES, default='Não')
    infecciosas_sarampo = models.CharField(max_length=40, verbose_name=_('Sarampo'), choices=YES_NO_CHOICES, default='Não')
    infecciosas_hepatite = models.CharField(max_length=40, verbose_name=_('Hepatite'), choices=YES_NO_CHOICES, default='Não')

    habitos_tabagismo = models.CharField(max_length=40, verbose_name=_('Tabagismo'), choices=YES_NO_CHOICES, default='Não')
    habitos_etilismo = models.CharField(max_length=40, verbose_name=_('Etilismo'), choices=YES_NO_CHOICES, default='Não')
    habitos_drogas = models.CharField(max_length=40, verbose_name=_('Drogas'), choices=YES_NO_CHOICES, default='Não')
    habitos_alimentacao = models.CharField(max_length=40, verbose_name=_('Alimentação'), choices=YES_NO_CHOICES, default='Não')
    habitos_medicamentos = models.CharField(max_length=40, verbose_name=_('Medicamentos'), choices=YES_NO_CHOICES, default='Não')

    historia_frequencia_diurno = models.CharField(max_length=40, verbose_name=_('Frequência da Micção (Diurno)'), blank=True)
    historia_frequencia_noturno = models.CharField(max_length=40, verbose_name=_('Frequência da Micção (Noturno)'), blank=True)
    historia_frequencia_total = models.CharField(max_length=40, verbose_name=_('Frequência da Micção (Total)'), blank=True)
    historia_perda = models.CharField(max_length=40, verbose_name=_('Tem perda de urina?'), choices=YES_NO_CHOICES, default='Não')
    historia_perda_total = models.CharField(max_length=40, verbose_name=_('Casos de Perda da Urina'), blank=True)
    historia_perda_tempo = models.CharField(max_length=40, verbose_name=_('Quando Ocorre Perda de Urina?'), choices=[('Após as atividades', 'Após as atividades'), ('Ao mesmo tempo que as atividades', 'Ao mesmo tempo que as atividades')], blank=True)
    historia_perda_comeco = models.CharField(max_length=40, verbose_name=_('Quando Começou a Perda de Urina?'), choices=[('Durante gestação', 'Durante gestação'), ('Depois da gestação', 'Depois da gestação'), ('Após cirurgia vaginal/abdominal', 'Após cirurgia vaginal/abdominal'), ('Depois da cesariana', 'Depois da cesariana')], blank=True)
    historia_vontade = models.CharField(max_length=40, verbose_name=_('Como é a vontade de urinar?'), choices=[('Urgente', 'Urgente'), ('Controlada', 'Controlada')], blank=True)
    historia_dor = models.CharField(max_length=40, verbose_name=_('Existe Dor ao Urinar?'), choices=YES_NO_CHOICES, default='Não')
    historia_urina_cor = models.CharField(max_length=40, verbose_name=_('Cor da Urina'), blank=True)
    historia_urina_odor = models.CharField(max_length=40, verbose_name=_('Odor da Urina'), blank=True)

    exame_pa = models.CharField(max_length=40, verbose_name=_('PA'), blank=True)
    exame_fc = models.CharField(max_length=40, verbose_name=_('FC'), blank=True)
    exame_t = models.CharField(max_length=40, verbose_name=_('T'), blank=True)
    exame_fr = models.CharField(max_length=40, verbose_name=_('FR'), blank=True)
    exame_respiracao = models.CharField(max_length=40, verbose_name=_('Tipo de Respiração'), blank=True)

    seios_volume = models.CharField(max_length=40, verbose_name=_('Volume'), choices=[('Aumentado', 'Aumentado'), ('Normal', 'Normal'), ('Diminuído', 'Diminuído')], blank=True)
    seios_temperatura = models.CharField(max_length=40, verbose_name=_('Temperatura'), choices=[('Aumentada', 'Aumentada'), ('Normal', 'Normal'), ('Diminuída', 'Diminuída')], blank=True)
    seios_circulacao = models.CharField(max_length=40, verbose_name=_('Circulação Cutânea'), choices=[('Aumentada', 'Aumentada'), ('Normal', 'Normal'), ('Diminuída', 'Diminuída')], blank=True)
    seios_mamilo = models.CharField(max_length=40, verbose_name=_('Tipo de Mamilo'), choices=[('Normal', 'Normal'), ('Raso', 'Raso'), ('Invertido', 'Invertido')], blank=True)
    seios_colostro = models.CharField(max_length=40, verbose_name=_('Colostro'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)
    seios_estrias = models.CharField(max_length=40, verbose_name=_('Estrias'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)
    seios_hiperpigmentacao = models.CharField(max_length=40, verbose_name=_('Hiperpigmentação'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)

    abdomem_hiperpigmentacao = models.CharField(max_length=40, verbose_name=_('Hiperpigmentação'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)
    abdomem_volume = models.CharField(max_length=40, verbose_name=_('Aumento de Volume'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)
    abdomem_estrias = models.CharField(max_length=40, verbose_name=_('Estrias'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)
    abdomem_cicatriz = models.CharField(max_length=40, verbose_name=_('Cicatriz'), choices=[('Normal', 'Normal'), ('Herniada', 'Herniada'), ('Plana', 'Plana')], blank=True)
    abdomem_altura = models.CharField(max_length=40, verbose_name=_('Altura Uterina'), blank=True)
    abdomem_circuferencia = models.CharField(max_length=40, verbose_name=_('Circuferência Abdominal'), blank=True)

    mmii_edema = models.CharField(max_length=40, verbose_name=_('Edema'), blank=True)
    mmii_varizes = models.CharField(max_length=40, verbose_name=_('Varizes'), blank=True)
    mmii_caimbras = models.CharField(max_length=40, verbose_name=_('Câimbras'), blank=True)
    mmii_dor = models.CharField(max_length=40, verbose_name=_('Dor'), blank=True)

    musculo_palpacao = models.CharField(max_length=40, verbose_name=_('Palpação do Períneo'), blank=True)
    musculo_contracao = models.CharField(max_length=40, verbose_name=_('Tempo de Contração'), blank=True)

    testes_especiais = models.TextField(verbose_name=_('Testes Especiais'), blank=True)

    diagnostico = models.TextField(verbose_name=_('Diagnóstico Fisioterapêutico'), blank=True)

    metas = models.TextField(verbose_name=_('Metas a Curto e Longo Prazo'), blank=True)

    recursos = models.TextField(verbose_name=_('Recursos Que Serão Utilizados Como Justificativa'), blank=True)

    class Meta:
        verbose_name = _('Avaliação Fisioterapêutica Gestacional')
        verbose_name_plural = _('Avaliações Fisioterapêutica Gestacional')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaAvaliacaoMasculina(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)
    data_atendimento = models.DateField(verbose_name=_('Data do Atendimento'), blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    registro = models.CharField(max_length=40, verbose_name=_('Registro'), blank=True)
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    funcao = models.CharField(max_length=40, verbose_name=_('Função'), blank=True)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    cep = models.CharField(max_length=40, verbose_name=_('CEP'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    celular = models.CharField(max_length=40, verbose_name=_('Celular'), blank=True)

    motivo = models.TextField(verbose_name=_('Motivo da Consulta'), blank=True)

    antecedentes_peso = models.CharField(max_length=40, verbose_name=_('Peso'), blank=True)
    antecedentes_altura = models.CharField(max_length=40, verbose_name=_('Altura'), blank=True)
    antecedentes_imc = models.CharField(max_length=40, verbose_name=_('IMC'), blank=True)
    antecedentes_intestino = models.CharField(max_length=40, verbose_name=_('Intestino'), choices=[('Normal', 'Normal'), ('Obstipado', 'Obstipado')], blank=True)
    antecedentes_infeccoes = models.CharField(max_length=40, verbose_name=_('Infecções'), choices=[('Anteriores', 'Anteriores'), ('Repetições', 'Repetições'), ('Atual', 'Atual')], blank=True)
    antecedentes_freq_miccional = models.CharField(max_length=40, verbose_name=_('Frequência Miccional'), choices=[('Diurna', 'Diurna'), ('Noturna', 'Noturna')], blank=True)
    antecedentes_esvaziamento = models.CharField(max_length=40, verbose_name=_('Sensação de Esvaziamento Vesical'), choices=[('Completo', 'Completo'), ('Incompleto', 'Incompleto')], blank=True)
    antecedentes_gotejamento = models.CharField(max_length=40, verbose_name=_('Gotejamento Pós-Miccional'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_urgencia = models.CharField(max_length=40, verbose_name=_('Urgência Miccional'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_perda = models.CharField(max_length=40, verbose_name=_('Sensação de Perda'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_iue = models.CharField(max_length=40, verbose_name=_('IUE'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_tosse = models.CharField(max_length=40, verbose_name=_('Tosse'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_espirro = models.CharField(max_length=40, verbose_name=_('Espirro'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_riso = models.CharField(max_length=40, verbose_name=_('Riso Forçado'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_atividade = models.CharField(max_length=40, verbose_name=_('Atividade Física'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_esporte = models.CharField(max_length=40, verbose_name=_('Esporte'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_sexual = models.CharField(max_length=40, verbose_name=_('Relação Sexual'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_marcha = models.CharField(max_length=40, verbose_name=_('Marcha'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_corrida = models.CharField(max_length=40, verbose_name=_('Corrida'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_carregamento_peso = models.CharField(max_length=40, verbose_name=_('Carregamento de Peso'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_posicao = models.CharField(max_length=40, verbose_name=_('Mudança de Posição'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_forros = models.CharField(max_length=40, verbose_name=_('Troca de Forros'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_cigarro = models.CharField(max_length=40, verbose_name=_('Cigarro'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_alcool = models.CharField(max_length=40, verbose_name=_('Álcool'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_habitos = models.TextField(verbose_name=_('Hábitos de Vida'), blank=True)
    antecedentes_cirurgia = models.TextField(max_length=40, verbose_name=_('Cirurgias Anteriores'), blank=True)
    antecedentes_medicacoes = models.TextField(verbose_name=_('Medicações Atuais'), blank=True)

    doencas_atuais = models.TextField(verbose_name=_('Doenças Atuais'), blank=True)
    doencas_neurologicas = models.TextField(verbose_name=_('Doenças Neurológicas'), blank=True)
    doencas_ortopedicas = models.TextField(verbose_name=_('Doenças Ortopédicas'), blank=True)
    doencas_psiquiatricas = models.TextField(verbose_name=_('Doenças Psiquiátricas'), blank=True)
    doencas_bronquite_tosse = models.TextField(verbose_name=_('Bronquite ou Tosse'), blank=True)
    doencas_diabetes = models.TextField(verbose_name=_('Diabetes'), blank=True)
    doencas_gerais = models.TextField(verbose_name=_('Doenças Gerais'), blank=True)
    doencas_satisfacao = models.CharField(max_length=40, verbose_name=_('Grau de Satisfação com a Situação Atual'), choices=[('Satisfeito', 'Satisfeito'), ('Insatisfeito', 'Insatisfeito'), ('Indiferente', 'Indiferente')], blank=True)

    dados_urodinamicos = models.TextField(verbose_name=_('Pré-Tratamento - Considerar Resultados Médicos'), blank=True)

    exame_fisico = models.TextField(verbose_name=_('Avaliação Postural'), blank=True)

    exame_pele = models.CharField(max_length=40, verbose_name=_('Estado da Pele'), choices=[('Atrófica', 'Atrófica'), ('Normal', 'Normal')], blank=True)
    exame_pele_inspecao = models.CharField(max_length=40, verbose_name=_('Inspeção da Pele'), choices=[('Mucosa Hipeêmica', 'Mucosa Hipeêmica'), ('Presença de irritação local', 'Presença de irritação local '), ('Presença de Corrimentos', 'Presença de Corrimentos'), ('Presença de cicatrizes', 'Presença de cicatrizes'), ('Presença de Varicosidades', 'resença de Varicosidades')], blank=True)
    exame_cicatriz = models.CharField(max_length=40, verbose_name=_('Cicatrizes/Aderências'), blank=True)
    exame_zonas = models.CharField(max_length=40, verbose_name=_('Zonas Doloras'), blank=True)
    exame_hernias = models.CharField(max_length=40, verbose_name=_('Hérnias'), blank=True)
    exame_diastase = models.CharField(max_length=40, verbose_name=_('Diástase'), blank=True)
    exame_nucleo_fibroso = models.CharField(max_length=40, verbose_name=_('Núcleo Fibroso Central do Príneo'), choices=[('Hipotônico (Depressão)', 'Hipotônico (Depressão)'), ('Normal (Resist. Elástica)', 'Normal (Resist. Elástica)'), ('Hipertônico (Resist. Rígida)', 'Hipertônico (Resist. Rígida)')], blank=True)
    exame_forca = models.CharField(max_length=40, verbose_name=_('Força Muscular'), choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True)

    avaliacao_funcional = models.CharField(max_length=40, verbose_name=_('AFA'), choices=[('Grau 0', 'Sem função perineal objetiva, nem mesmo à palpitação'), ('Grau 1', 'Função perineal objetiva ausente, contração reconhecível somente à palpação.'), ('Grau 2', 'Função perineal objetiva débil, reconhecida à palpação.'), ('Grau 3', 'Função perineal objetiva presente e resistência opositora à palpação; não mantida'), ('Grau 4', 'Função perineal objetiva presente e resistência opositora mantida mais que cinco segundos')], blank=True)
    avaliacao_apneia = models.CharField(max_length=40, verbose_name=_('Apneia'), choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], blank=True)
    avaliacao_participacao = models.CharField(max_length=40, verbose_name=_('Participação de Músculos Acessórios'), choices=[('Abdominais', 'Abdominais'), ('Glúteos', 'Glúteos'), ('Adutores', 'Adutores')], blank=True)
    avaliacao_testes = models.TextField(verbose_name=_('Testes Especiais (Se Houver Necessidade)'), blank=True)
    avaliacao_diagnostico = models.TextField(verbose_name=_('Diagnóstico Fisioterapêutico'), blank=True)
    avaliacao_metas = models.TextField(verbose_name=_('Metas a Curto e Longo Prazo'), blank=True)
    avaliacao_recursos = models.TextField(verbose_name=_('Recursos Que Serão Utilizados Com Justificativa'), blank=True)

    aluno = models.CharField(max_length=40, verbose_name=_('Nome do Aluno'), blank=True)

    class Meta:
        verbose_name = _('Avaliação de Incontinência Urinária Masculina')
        verbose_name_plural = _('Avaliações de Incontinência Urinária Masculina')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaAvaliacaoFeminina(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)
    data_atendimento = models.DateField(verbose_name=_('Data do Atendimento'), blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    registro = models.CharField(max_length=40, verbose_name=_('Registro'), blank=True)
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    funcao = models.CharField(max_length=40, verbose_name=_('Função'), blank=True)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    cep = models.CharField(max_length=40, verbose_name=_('CEP'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    celular = models.CharField(max_length=40, verbose_name=_('Celular'), blank=True)

    motivo = models.TextField(verbose_name=_('Motivo da Consulta'), blank=True)

    antecedentes_obesa = models.CharField(max_length=40, verbose_name=_('Obesa'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_gravidez = models.CharField(max_length=40, verbose_name=_('Gravidez'), blank=True)
    antecedentes_forros = models.CharField(max_length=40, verbose_name=_('Troca de Forros'), choices=YES_NO_CHOICES, blank=True)
    antecedentes_cirurgia = models.TextField(max_length=40, verbose_name=_('Cirurgias Anteriores'), blank=True)
    antecedentes_medicacoes = models.TextField(verbose_name=_('Medicações Atuais'), blank=True)

    doencas_atuais = models.TextField(verbose_name=_('Doenças Atuais'), blank=True)
    doencas_neurologicas = models.TextField(verbose_name=_('Doenças Neurológicas'), blank=True)
    doencas_ortopedicas = models.TextField(verbose_name=_('Doenças Ortopédicas'), blank=True)
    doencas_psiquiatricas = models.TextField(verbose_name=_('Doenças Psiquiátricas'), blank=True)
    doencas_bronquite_tosse = models.TextField(verbose_name=_('Bronquite ou Tosse'), blank=True)
    doencas_diabetes = models.TextField(verbose_name=_('Diabetes'), blank=True)
    doencas_gerais = models.TextField(verbose_name=_('Doenças Gerais'), blank=True)
    doencas_satisfacao = models.CharField(max_length=40, verbose_name=_('Grau de Satisfação com a Situação Atual'), choices=[('Satisfeito', 'Satisfeito'), ('Insatisfeito', 'Insatisfeito'), ('Indiferente', 'Indiferente')], blank=True)

    dados_urodinamicos = models.TextField(verbose_name=_('Pré-Tratamento - Considerar Resultados Médicos'), blank=True)

    partos_normal = models.CharField(max_length=40, verbose_name=_('Normal'), blank=True)
    partos_forceps = models.CharField(max_length=40, verbose_name=_('Fórceps'), blank=True)
    partos_cesareas = models.CharField(max_length=40, verbose_name=_('Cesáreas'), blank=True)
    partos_abortos = models.CharField(max_length=40, verbose_name=_('Abortos'), blank=True)

    habitos_cigarro = models.CharField(max_length=40, verbose_name=_('Cigarro (Quantidade/Dia)'), blank=True)
    habitos_alcool = models.CharField(max_length=40, verbose_name=_('Álcool (Dose/Dia)'), blank=True)
    habitos_alimentacao = models.CharField(max_length=40, verbose_name=_('Alimentação'), blank=True)
    habitos_atividade = models.TextField(verbose_name=_('Atividade Física'), blank=True)

    infeccoes_anteriores = models.TextField(verbose_name=_('Anteriores'), blank=True)
    infeccoes_disuria = models.CharField(max_length=40, verbose_name=_('Presença de Disúria'), blank=True)
    infeccoes_hematuria = models.CharField(max_length=40, verbose_name=_('Hematúria'), blank=True)

    miccicional_frequencia = models.CharField(max_length=40, verbose_name=_('Frequência Miccional'), blank=True)
    miccicional_esvaziamento = models.CharField(max_length=40, verbose_name=_('Sensação de Esvaziamento Vesical'), blank=True, choices=[('Completo', 'Completo'), ('Incompleto', 'Incompleto')])
    miccicional_gotejamento = models.CharField(max_length=40, verbose_name=_('Gotejamento Pós-Micional'), blank=True, choices=YES_NO_CHOICES)
    miccicional_urgencia = models.CharField(max_length=40, verbose_name=_('Urgência Micional'), blank=True, choices=YES_NO_CHOICES)
    miccicional_iue = models.CharField(max_length=40, verbose_name=_('Investigação de IUE'), blank=True)

    perda_tosse = models.CharField(max_length=40, verbose_name=_('Tosse'), blank=True, choices=YES_NO_CHOICES)
    perda_espirro = models.CharField(max_length=40, verbose_name=_('Espirro'), blank=True, choices=YES_NO_CHOICES)
    perda_riso = models.CharField(max_length=40, verbose_name=_('Riso Forçado'), blank=True, choices=YES_NO_CHOICES)
    perda_atividade = models.CharField(max_length=40, verbose_name=_('Atividade Física'), blank=True, choices=YES_NO_CHOICES)
    perda_esporte = models.CharField(max_length=40, verbose_name=_('Esporte'), blank=True, choices=YES_NO_CHOICES)
    perda_relacao = models.CharField(max_length=40, verbose_name=_('Relação Sexual'), blank=True, choices=YES_NO_CHOICES)
    perda_marcha = models.CharField(max_length=40, verbose_name=_('Marcha'), blank=True, choices=YES_NO_CHOICES)
    perda_corrida = models.CharField(max_length=40, verbose_name=_('Corrida'), blank=True, choices=YES_NO_CHOICES)
    perda_carregamento = models.CharField(max_length=40, verbose_name=_('Carregamento de Peso'), blank=True, choices=YES_NO_CHOICES)
    perda_posicao = models.CharField(max_length=40, verbose_name=_('Mudança de Posição'), blank=True, choices=YES_NO_CHOICES)

    exame_peso = models.CharField(max_length=40, verbose_name=_('Peso (Kg)'), blank=True)
    exame_altura = models.CharField(max_length=40, verbose_name=_('Altura (m)'), blank=True)
    exame_imc = models.CharField(max_length=40, verbose_name=_('IMC (Kg/m²)'), blank=True)
    exame_postural = models.TextField(verbose_name=_('Avaliação Postural'), blank=True)

    exame_pele = models.CharField(max_length=40, verbose_name=_('Estado da Pele'), choices=[('Atrófica', 'Atrófica'), ('Normal', 'Normal')], blank=True)
    exame_estrias = models.CharField(max_length=40, verbose_name=_('Estrias'), choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], blank=True)
    exame_pele_inspecao = models.CharField(max_length=40, verbose_name=_('Inspeção da Pele'), choices=[('Mucosa Hipeêmica', 'Mucosa Hipeêmica'), ('Presença de irritação local', 'Presença de irritação local '), ('Presença de Corrimentos', 'Presença de Corrimentos'), ('Presença de cicatrizes', 'Presença de cicatrizes'), ('Presença de Varicosidades', 'Presença de Varicosidades'), ('Presença de Epsiotomias', 'Presença de Epsiotomias')], blank=True)
    exame_cicatriz = models.CharField(max_length=40, verbose_name=_('Cicatrizes/Aderências'), blank=True)
    exame_zonas = models.CharField(max_length=40, verbose_name=_('Zonas Doloras'), blank=True)
    exame_hernias = models.CharField(max_length=40, verbose_name=_('Hérnias'), blank=True)
    exame_diastase = models.CharField(max_length=40, verbose_name=_('Diástase'), blank=True)
    exame_nucleo_fibroso = models.CharField(max_length=40, verbose_name=_('Núcleo Fibroso Central do Príneo'), choices=[('Hipotônico (Depressão)', 'Hipotônico (Depressão)'), ('Normal (Resist. Elástica)', 'Normal (Resist. Elástica)'), ('Hipertônico (Resist. Rígida)', 'Hipertônico (Resist. Rígida)')], blank=True)
    exame_forca = models.CharField(max_length=40, verbose_name=_('Força Muscular'), choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True)

    palpacao_exploracao = models.CharField(max_length=40, verbose_name=_('Exploração do Canal Vaginal (unidigital)'), blank=True)
    palpacao_zonas = models.CharField(max_length=40, verbose_name=_('Zonas Dolorosas'), blank=True)
    palpacao_trigger = models.CharField(max_length=40, verbose_name=_('Trigger Points'), blank=True)
    palpacao_laceracao = models.CharField(max_length=40, verbose_name=_('Laceração Musculas'), blank=True)

    avaliacao_funcional = models.CharField(max_length=40, verbose_name=_('AFA'), choices=[('Grau 0', 'Sem função perineal objetiva, nem mesmo à palpitação'), ('Grau 1', 'Função perineal objetiva ausente, contração reconhecível somente à palpação.'), ('Grau 2', 'Função perineal objetiva débil, reconhecida à palpação.'), ('Grau 3', 'Função perineal objetiva presente e resistência opositora à palpação; não mantida'), ('Grau 4', 'Função perineal objetiva presente e resistência opositora mantida mais que cinco segundos')], blank=True)
    avaliacao_tempo = models.CharField(max_length=40, verbose_name=_('Tempo de Manutenção da Contração (AFA-Bidigital)'), blank=True)
    avaliacao_apneia = models.CharField(max_length=40, verbose_name=_('Apneia'), choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], blank=True)
    avaliacao_participacao = models.CharField(max_length=40, verbose_name=_('Participação de Músculos Acessórios'), choices=[('Abdominais', 'Abdominais'), ('Glúteos', 'Glúteos'), ('Adutores', 'Adutores')], blank=True)
    avaliacao_perineometro_pico = models.CharField(max_length=40, verbose_name=_('Perineômetro Pico'), blank=True)
    avaliacao_perineometro_manutencao = models.CharField(max_length=40, verbose_name=_('Tempo Manutenção do Pico'), blank=True)
    avaliacao_bulbo = models.CharField(max_length=40, verbose_name=_('Bulbocavernoso'), choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], blank=True)
    avaliacao_cultaneo = models.CharField(max_length=40, verbose_name=_('Cutâneo Anal'), choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], blank=True)
    avaliacao_tosse = models.CharField(max_length=40, verbose_name=_('Teste da Tosse'), choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], blank=True)
    avaliacao_testes = models.TextField(verbose_name=_('Testes Especiais (Se Houver Necessidade)'), blank=True)
    avaliacao_diagnostico = models.TextField(verbose_name=_('Diagnóstico Fisioterapêutico'), blank=True)
    avaliacao_metas = models.TextField(verbose_name=_('Metas a Curto e Longo Prazo'), blank=True)
    avaliacao_recursos = models.TextField(verbose_name=_('Recursos Que Serão Utilizados Com Justificativa'), blank=True)

    aluno = models.CharField(max_length=40, verbose_name=_('Nome do Aluno'), blank=True)

    class Meta:
        verbose_name = _('Avaliação de Incontinência Urinária Feminina')
        verbose_name_plural = _('Avaliações de Incontinência Urinária Feminina')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaAcidenteVascularEncefalico(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    diagnostico_clinico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Fisioterápico'), blank=True)

    dados_pa = models.CharField(max_length=40, verbose_name=_('P.A.'), blank=True)
    dados_fc = models.CharField(max_length=40, verbose_name=_('F.C.'), blank=True)
    dados_fr = models.CharField(max_length=40, verbose_name=_('F.R.'), blank=True)
    dados_t = models.CharField(max_length=40, verbose_name=_('T°'), blank=True)

    medicamentos_utilizados = models.TextField(verbose_name=_('Medicamentos Utilizados'), blank=True)

    patologias_hipertensao = models.CharField(max_length=1, verbose_name=_('Hipertensão Arterial'), choices=YES_NO_CHOICES, blank=True)
    patologias_cardiopatias = models.CharField(max_length=1, verbose_name=_('Cardiopatias'), choices=YES_NO_CHOICES, blank=True)
    patologias_diabetes = models.CharField(max_length=1, verbose_name=_('Diabetes'), choices=YES_NO_CHOICES, blank=True)
    patologias_articular = models.CharField(max_length=1, verbose_name=_('Comprometimento Articular'), choices=YES_NO_CHOICES, blank=True)
    patologias_alergias = models.CharField(max_length=1, verbose_name=_('Alergias'), choices=YES_NO_CHOICES, blank=True)
    patologias_dor = models.CharField(max_length=1, verbose_name=_('Dor'), choices=YES_NO_CHOICES, blank=True)
    patologias_outras = models.TextField(verbose_name=_('Outras'), blank=True)
    patologias_cirurgico = models.TextField(verbose_name=_('Antecedentes Cirúrgicos'), blank=True)

    anamnese_qp = models.TextField(verbose_name=_('Q.P.'), blank=True)
    anamnese_lesao = models.CharField(max_length=40, verbose_name=_('H.M.P.A.: Tempo da Lesão'), blank=True)
    anamnese_tratamento = models.CharField(max_length=40, verbose_name=_('Tratamento Fisioterápico'), choices=YES_NO_CHOICES, blank=True)

    exame_atitude = models.CharField(max_length=40, verbose_name=_('Atitude'), choices=[('Ativo', 'Ativo'), ('Passivo', 'Passivo')], blank=True)
    exame_consciencia = models.CharField(max_length=40, verbose_name=_('Nível de Consciência'), choices=[('Bom', 'Bom'), ('Regular', 'Regular'), ('Ruim', 'Ruim')], blank=True)
    exame_postura = models.TextField(verbose_name=_('Postura'), blank=True)
    exame_marcha = models.TextField(verbose_name=_('Exame da Marcha'), blank=True)
    exame_retracao_encurtamento = models.TextField(verbose_name=_('Retrações e Encurtamentos'), blank=True)
    exame_deformidades = models.TextField(verbose_name=_('Deformidades'), blank=True)

    movimentos_coreia = models.CharField(max_length=40, verbose_name=_('Coréia'), choices=YES_NO_CHOICES, blank=True)
    movimentos_atetose = models.CharField(max_length=40, verbose_name=_('Atetose'), choices=YES_NO_CHOICES, blank=True)
    movimentos_balismo = models.CharField(max_length=40, verbose_name=_('Balismo'), choices=YES_NO_CHOICES, blank=True)
    movimentos_tremor = models.CharField(max_length=40, verbose_name=_('Tremor'), choices=YES_NO_CHOICES, blank=True)
    movimentos_mioclonia = models.CharField(max_length=40, verbose_name=_('Mioclonias'), choices=YES_NO_CHOICES, blank=True)
    movimentos_fasciculacoes = models.CharField(max_length=40, verbose_name=_('Fasciculações'), choices=YES_NO_CHOICES, blank=True)
    movimentos_outros = models.TextField(verbose_name=_('Outros'), blank=True)

    coordenacao_decomposicao = models.CharField(max_length=40, verbose_name=_('Decomposição de Movimento'), choices=YES_NO_CHOICES, blank=True)
    coordenacao_dismetria = models.CharField(max_length=40, verbose_name=_('Dismetria'), choices=YES_NO_CHOICES, blank=True)
    coordenacao_rechaco = models.CharField(max_length=40, verbose_name=_('Rechaço de Stewart-Holmes'), choices=YES_NO_CHOICES, blank=True)
    coordenacao_ataxia = models.CharField(max_length=40, verbose_name=_('Ataxia Crebelar'), choices=YES_NO_CHOICES, blank=True)
    coordenacao_nistagmo = models.CharField(max_length=40, verbose_name=_('Nistagmo'), choices=YES_NO_CHOICES, blank=True)

    equilibrio = models.TextField(verbose_name=_('Equilíbrio'), blank=True)

    escala_grau = models.CharField(max_length=40, verbose_name=_('Tônus Asworth'), choices=[('Grau 1', 'Grau 1: Tônus normal.'), ('Grau 2', 'Grau 2: Aumento leve do tônus - movimentação passiva com certa resistência.'), ('Grau 3', 'Grau 3: Aumento moderado do tônus - maior resistência à movimentação passiva.'), ('Grau 4', 'Grau 4: Aumento considerável do tônus - movimentação passiva é difícil.'), ('Grau 5', 'Grau 5: Rigidez em flexão ou extensão.')], blank=True)
    escala_perimetria = models.CharField(max_length=40, verbose_name=_('Perimetria'), choices=[('Normal', 'Normal'), ('Alterada', 'Alterada'), ('Discrepância', 'Discrepância')], blank=True)
    escala_trofismo = models.CharField(max_length=40, verbose_name=_('Trofismo'), choices=[('Normo', 'Normo'), ('Hipertrofia', 'Hipertrofia'), ('Hipotrofia', 'Hipotrofia')], blank=True)

    mmss = models.CharField(max_length=40, verbose_name=_('MMSS'), blank=True)
    mmss_direito_7 = models.CharField(max_length=40, verbose_name=_('Direito - 7cm'), blank=True)
    mmss_direito_14 = models.CharField(max_length=40, verbose_name=_('Direito - 14cm'), blank=True)
    mmss_direito_21 = models.CharField(max_length=40, verbose_name=_('Direito - 21cm'), blank=True)
    mmss_esquerdo_7 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 7cm'), blank=True)
    mmss_esquerdo_14 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 14cm'), blank=True)
    mmss_esquerdo_21 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 21cm'), blank=True)

    mmii = models.CharField(max_length=40, verbose_name=_('MMII'), blank=True)
    mmii_direito_7 = models.CharField(max_length=40, verbose_name=_('Direito - 7cm'), blank=True)
    mmii_direito_14 = models.CharField(max_length=40, verbose_name=_('Direito - 14cm'), blank=True)
    mmii_direito_21 = models.CharField(max_length=40, verbose_name=_('Direito - 21cm'), blank=True)
    mmii_esquerdo_7 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 7cm'), blank=True)
    mmii_esquerdo_14 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 14cm'), blank=True)
    mmii_esquerdo_21 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 21cm'), blank=True)

    reflexos_bicipital = models.CharField(max_length=40, verbose_name=_('Bicipital - C6'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_tricipital = models.CharField(max_length=40, verbose_name=_('Tricipital - C7'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_patelar = models.CharField(max_length=40, verbose_name=_('Patelar - L2, L3 e L4'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_anquileu = models.CharField(max_length=40, verbose_name=_('Anquileu - L5, S1 e S2'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)

    sensibilidade_superficial = models.CharField(max_length=40, verbose_name=_('Sensibilidade Superficial (Exterioceptiva)'), blank=True)
    sensibilidade_tatil = models.CharField(max_length=40, verbose_name=_('Tátil'), choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], blank=True)
    sensibilidade_termica = models.CharField(max_length=40, verbose_name=_('Térmica e Dolorosa'), choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], blank=True)
    sensibilidade_profunda = models.CharField(max_length=40, verbose_name=_('Sensibilidade Profunda'), blank=True)
    sensibilidade_cinetica = models.CharField(max_length=40, verbose_name=_('Cinética - Postural'), choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], blank=True)
    sensibilidade_combinada = models.CharField(max_length=40, verbose_name=_('Sensibilidade Combinada'), blank=True)
    sensibilidade_topognosia = models.CharField(max_length=40, verbose_name=_('Topognosia'), choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], blank=True)
    sensibilidade_esterognosia = models.CharField(max_length=40, verbose_name=_('Esterognosia'), choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], blank=True)
    sensibilidade_barognosia = models.CharField(max_length=40, verbose_name=_('Barognosia'), choices=[('Preservada', 'Preservada'), ('Alterada', 'Alterada')], blank=True)

    ms_direito_ombro = models.CharField(max_length=40, verbose_name=_('Ombro'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_direito_cotovelo = models.CharField(max_length=40, verbose_name=_('Cotovelo'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_direito_punho = models.CharField(max_length=40, verbose_name=_('Punho'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_direito_mao = models.CharField(max_length=40, verbose_name=_('Mão'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_direito_dedos = models.CharField(max_length=40, verbose_name=_('Dedos'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)

    ms_esquerdo_ombro = models.CharField(max_length=40, verbose_name=_('Ombro'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_esquerdo_cotovelo = models.CharField(max_length=40, verbose_name=_('Cotovelo'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_esquerdo_punho = models.CharField(max_length=40, verbose_name=_('Punho'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_esquerdo_mao = models.CharField(max_length=40, verbose_name=_('Mão'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    ms_esquerdo_dedos = models.CharField(max_length=40, verbose_name=_('Dedos'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)

    mi_direito_quadril = models.CharField(max_length=40, verbose_name=_('Quadril'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    mi_direito_joelho = models.CharField(max_length=40, verbose_name=_('Joelho'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    mi_direito_tornozelo = models.CharField(max_length=40, verbose_name=_('Tornozelo'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    mi_direito_pe = models.CharField(max_length=40, verbose_name=_('Pé'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)

    mi_esquerdo_quadril = models.CharField(max_length=40, verbose_name=_('Quadril'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    mi_esquerdo_joelho = models.CharField(max_length=40, verbose_name=_('Joelho'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    mi_esquerdo_tornozelo = models.CharField(max_length=40, verbose_name=_('Tornozelo'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)
    mi_esquerdo_pe = models.CharField(max_length=40, verbose_name=_('Pé'), choices=[('N', 'Normal'), ('R', 'Reduzida')], blank=True)

    desenvolvimento_avds = models.CharField(max_length=40, verbose_name=_('AVD\'s'), choices=[('Independente', 'Independente'), ('Dependente', 'Dependente'), ('Semi-Independente', 'Semi-Independente')], blank=True)
    desenvolvimento_neurofuncional = models.TextField(verbose_name=_('NeuroFuncional'), blank=True)

    objetivos_tratamento = models.TextField(verbose_name=_('Tratamento'), blank=True)
    objetivos_conduta = models.TextField(verbose_name=_('Conduta Fisioterapêutica'), blank=True)

    atendimento_estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)
    atendimento_supervisor = models.CharField(max_length=40, verbose_name=_('Supervissor (a)'), blank=True)

    class Meta:
        verbose_name = _('Avaliação Acidente Vascular Encefálico')
        verbose_name_plural = _('Avaliações Acidente Vascular Encefálico')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaEscleroseMultipla(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)

    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    diagnostico_clinico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Fisioterápico'), blank=True)

    dados_pa = models.CharField(max_length=40, verbose_name=_('P.A.'), blank=True)
    dados_fc = models.CharField(max_length=40, verbose_name=_('F.C.'), blank=True)
    dados_fr = models.CharField(max_length=40, verbose_name=_('F.R.'), blank=True)
    dados_t = models.CharField(max_length=40, verbose_name=_('T°'), blank=True)

    info_medicamentos = models.TextField(verbose_name=_('Medicamentos Utilizados'), blank=True)
    info_exames = models.TextField(verbose_name=_('Exames Complementares'), blank=True)
    info_antecedentes = models.TextField(verbose_name=_('Antecedentes Cirúrgicos'), blank=True)
    info_adm = models.TextField(verbose_name=_('ADM'), blank=True)

    anamnese_qp = models.TextField(verbose_name=_('Q.P.'), blank=True)
    anamnese_hmpa = models.TextField(verbose_name=_('H.M.P.A.'), blank=True)

    exame_tonus = models.CharField(max_length=40, verbose_name=_('Escala de Avaliação do Tônus Asworth'), choices=[('Grau 1', 'Grau 1: Tônus normal.'), ('Grau 2', 'Grau 2: Aumento leve do tônus - movimentação passiva com certa resistência.'), ('Grau 3', 'Grau 3: Aumento moderado do tônus - maior resistência à movimentação passiva.'), ('Grau 4', 'Grau 4: Aumento considerável do tônus - movimentação passiva é difícil.'), ('Grau 5', 'Grau 5: Rigidez em flexão ou extensão.')], blank=True)
    exame_trofismo = models.CharField(max_length=40, verbose_name=_('Trofismo'), choices=[('Normo', 'Normo'), ('Hipertrofia', 'Hipertrofia'), ('Hipotrofia', 'Hipotrofia')], blank=True)

    reflexos_bicipital = models.CharField(max_length=40, verbose_name=_('Bicipital'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_tricipital = models.CharField(max_length=40, verbose_name=_('Tricipital'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_patelar = models.CharField(max_length=40, verbose_name=_('Patelar'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_anquileu = models.CharField(max_length=40, verbose_name=_('Anquileu'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)

    mmss = models.CharField(max_length=40, verbose_name=_('MMSS'), blank=True)
    mmss_direito_7 = models.CharField(max_length=40, verbose_name=_('Direito - 7cm'), blank=True)
    mmss_direito_14 = models.CharField(max_length=40, verbose_name=_('Direito - 14cm'), blank=True)
    mmss_direito_21 = models.CharField(max_length=40, verbose_name=_('Direito - 21cm'), blank=True)
    mmss_esquerdo_7 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 7cm'), blank=True)
    mmss_esquerdo_14 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 14cm'), blank=True)
    mmss_esquerdo_21 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 21cm'), blank=True)

    mmii = models.CharField(max_length=40, verbose_name=_('MMII'), blank=True)
    mmii_direito_7 = models.CharField(max_length=40, verbose_name=_('Direito - 7cm'), blank=True)
    mmii_direito_14 = models.CharField(max_length=40, verbose_name=_('Direito - 14cm'), blank=True)
    mmii_direito_21 = models.CharField(max_length=40, verbose_name=_('Direito - 21cm'), blank=True)
    mmii_esquerdo_7 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 7cm'), blank=True)
    mmii_esquerdo_14 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 14cm'), blank=True)
    mmii_esquerdo_21 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 21cm'), blank=True)

    desenvolvimento_avds = models.CharField(max_length=40, verbose_name=_('AVD\'s'), choices=[('Independente', 'Independente'), ('Dependente', 'Dependente'), ('Semi-Independente', 'Semi-Independente')], blank=True)
    desenvolvimento_neurofuncional = models.TextField(verbose_name=_('NeuroFuncional'), blank=True)
    desenvolvimento_conduta = models.TextField(verbose_name=_('Conduta Fisioterapêutica'), blank=True)

    kurtzke_piramidais = models.CharField(max_length=40, verbose_name=_('Funções Piramidais'), choices=[('0', 'Normal'), ('1', 'Sinais anormais sem incapacidades'), ('2', 'Incapacidade mínima'), ('3', 'Paraparesia ou Hemiparesia leve ou moderada, Monoparesia grave'), ('4', 'Paraparesia ou Hemiparesia acentuada, Quadriparesia moderada; ou Monoplegia'), ('5', 'Paraplegia, Hemiplegia ou Quadriparesia acentuada'), ('6', 'Quadriplegia')], blank=True)
    kurtzke_cerebelares = models.TextField(verbose_name=_('Funções Cerebelares'), blank=True)

    atendimento_estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)
    atendimento_supervisor = models.CharField(max_length=40, verbose_name=_('Supervissor (a)'), blank=True)

    class Meta:
        verbose_name = _('Avaliação Esclerose Múltipla')
        verbose_name_plural = _('Avaliações Esclerose Múltipla')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaTRM(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)

    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    diagnostico_clinico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Fisioterápico'), blank=True)

    dados_pa = models.CharField(max_length=40, verbose_name=_('P.A.'), blank=True)
    dados_fc = models.CharField(max_length=40, verbose_name=_('F.C.'), blank=True)
    dados_fr = models.CharField(max_length=40, verbose_name=_('F.R.'), blank=True)
    dados_t = models.CharField(max_length=40, verbose_name=_('T°'), blank=True)

    info_medicamentos = models.TextField(verbose_name=_('Medicamentos Utilizados'), blank=True)
    info_exames = models.TextField(verbose_name=_('Exames Complementares'), blank=True)
    info_antecedentes = models.TextField(verbose_name=_('Antecedentes Cirúrgicos'), blank=True)
    info_adm = models.TextField(verbose_name=_('ADM'), blank=True)

    anamnese_qp = models.TextField(verbose_name=_('Q.P.'), blank=True)
    anamnese_hmpa = models.TextField(verbose_name=_('H.M.P.A.'), choices=[('Traumática', 'Traumática'), ('Não Traumática', 'Não Traumática')], blank=True)

    complicacoes_bexiga = models.CharField(max_length=40, verbose_name=_('Bexiga Neurogênica'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_disreflexia = models.CharField(max_length=40, verbose_name=_('Disreflexia Autonômica'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_escaras = models.CharField(max_length=40, verbose_name=_('Escaras'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_ossificacao = models.CharField(max_length=40, verbose_name=_('Ossificação Heterotópica'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_dor = models.CharField(max_length=40, verbose_name=_('Dor'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_hipotensao = models.CharField(max_length=40, verbose_name=_('Hipotensão Postural'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_disestesias = models.CharField(max_length=40, verbose_name=_('Disestesias Medulares'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_trombose = models.CharField(max_length=40, verbose_name=_('Trombose Venosa Profunda'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_respiratorias = models.CharField(max_length=40, verbose_name=_('Complicações Respiratórias'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_deformidades = models.CharField(max_length=40, verbose_name=_('Deformidades'), choices=YES_NO_CHOICES, blank=True)
    complicacoes_outros = models.TextField(verbose_name=_('Outros'), blank=True)

    sexual_relacao = models.CharField(max_length=40, verbose_name=_('Já teve relações sexuais?'), choices=YES_NO_CHOICES, blank=True)
    sexual_filhos = models.CharField(max_length=40, verbose_name=_('Tem filhos?'), choices=YES_NO_CHOICES, blank=True)
    sexual_vontade_filhos = models.CharField(max_length=40, verbose_name=_('Tem vontade de ter filhos?'), choices=YES_NO_CHOICES, blank=True)

    sexual_homem_erecao = models.CharField(max_length=40, verbose_name=_('Tem Ereção?'), choices=YES_NO_CHOICES, blank=True)
    sexual_homem_erecao_tipo = models.CharField(max_length=40, verbose_name=_('Tipo Ereção?'), choices=[('Reflexa', 'Reflexa'), ('Psicogênica', 'Psicogênica')], blank=True)
    sexual_homem_ejaculacao = models.CharField(max_length=40, verbose_name=_('Tem Ejaculação?'), choices=YES_NO_CHOICES, blank=True)
    sexual_homem_ejaculacao_tipo = models.CharField(max_length=40, verbose_name=_('Tipo Ejaculação?'), choices=[('Retrógrada', 'Retrógrada'), ('Normal', 'Normal')], blank=True)
    sexual_homem_orgasmo = models.CharField(max_length=40, verbose_name=_('Tem Orgasmo?'), choices=YES_NO_CHOICES, blank=True)

    sexual_mulher_orgasmo = models.CharField(max_length=40, verbose_name=_('Tem Orgasmo?'), choices=YES_NO_CHOICES, blank=True)
    sexual_mulher_lubrificacao = models.CharField(max_length=40, verbose_name=_('Tem Lubrificação?'), choices=YES_NO_CHOICES, blank=True)

    exame_tonus = models.CharField(max_length=40, verbose_name=_('Escala de Avaliação do Tônus Asworth'), choices=[('Grau 1', 'Grau 1: Tônus normal.'), ('Grau 2', 'Grau 2: Aumento leve do tônus - movimentação passiva com certa resistência.'), ('Grau 3', 'Grau 3: Aumento moderado do tônus - maior resistência à movimentação passiva.'), ('Grau 4', 'Grau 4: Aumento considerável do tônus - movimentação passiva é difícil.'), ('Grau 5', 'Grau 5: Rigidez em flexão ou extensão.')], blank=True)
    exame_trofismo = models.CharField(max_length=40, verbose_name=_('Trofismo'), choices=[('Normo', 'Normo'), ('Hipertrofia', 'Hipertrofia'), ('Hipotrofia', 'Hipotrofia')], blank=True)
    exame_tperimetria = models.CharField(max_length=40, verbose_name=_('Perimetria'), choices=[('Normal', 'Normal'), ('Alterada', 'Alterada')], blank=True)

    reflexos_bicipital = models.CharField(max_length=40, verbose_name=_('Bicipital'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_tricipital = models.CharField(max_length=40, verbose_name=_('Tricipital'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_patelar = models.CharField(max_length=40, verbose_name=_('Patelar'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_anquileu = models.CharField(max_length=40, verbose_name=_('Anquileu'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)

    mmss = models.CharField(max_length=40, verbose_name=_('MMSS'), blank=True)
    mmss_direito_7 = models.CharField(max_length=40, verbose_name=_('Direito - 7cm'), blank=True)
    mmss_direito_14 = models.CharField(max_length=40, verbose_name=_('Direito - 14cm'), blank=True)
    mmss_direito_21 = models.CharField(max_length=40, verbose_name=_('Direito - 21cm'), blank=True)
    mmss_esquerdo_7 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 7cm'), blank=True)
    mmss_esquerdo_14 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 14cm'), blank=True)
    mmss_esquerdo_21 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 21cm'), blank=True)

    mmii = models.CharField(max_length=40, verbose_name=_('MMII'), blank=True)
    mmii_direito_7 = models.CharField(max_length=40, verbose_name=_('Direito - 7cm'), blank=True)
    mmii_direito_14 = models.CharField(max_length=40, verbose_name=_('Direito - 14cm'), blank=True)
    mmii_direito_21 = models.CharField(max_length=40, verbose_name=_('Direito - 21cm'), blank=True)
    mmii_esquerdo_7 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 7cm'), blank=True)
    mmii_esquerdo_14 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 14cm'), blank=True)
    mmii_esquerdo_21 = models.CharField(max_length=40, verbose_name=_('Esquerdo - 21cm'), blank=True)

    desenvolvimento_avds = models.CharField(max_length=40, verbose_name=_('AVD\'s'), choices=[('Independente', 'Independente'), ('Dependente', 'Dependente'), ('Semi-Independente', 'Semi-Independente')], blank=True)
    desenvolvimento_neurofuncional = models.TextField(verbose_name=_('NeuroFuncional'), blank=True)
    desenvolvimento_conduta = models.TextField(verbose_name=_('Conduta Fisioterapêutica'), blank=True)
    desenvolvimento_objetivo = models.TextField(verbose_name=_('Objetivos de Tratamento'), blank=True)

    atendimento_estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)
    atendimento_supervisor = models.CharField(max_length=40, verbose_name=_('Supervissor (a)'), blank=True)

    class Meta:
        verbose_name = _('Avaliação TRM')
        verbose_name_plural = _('Avaliações TRM')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaNeurologica(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)

    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    diagnostico_clinico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Fisioterápico'), blank=True)

    dados_pa = models.CharField(max_length=40, verbose_name=_('P.A.'), blank=True)
    dados_fc = models.CharField(max_length=40, verbose_name=_('F.C.'), blank=True)
    dados_fr = models.CharField(max_length=40, verbose_name=_('F.R.'), blank=True)
    dados_t = models.CharField(max_length=40, verbose_name=_('T°'), blank=True)

    info_medicamentos = models.TextField(verbose_name=_('Medicamentos Utilizados'), blank=True)
    info_patologias = models.TextField(verbose_name=_('Patologias Associadas'), blank=True)
    info_antecedentes = models.TextField(verbose_name=_('Antecedentes Cirúrgicos'), blank=True)
    info_sensibilidade = models.TextField(verbose_name=_('Sensibilidade'), blank=True)

    anamnese_qp = models.TextField(verbose_name=_('Q.P.'), blank=True)
    anamnese_hmpa = models.TextField(verbose_name=_('H.M.A.'), blank=True)
    anamnese_hp = models.TextField(verbose_name=_('H.P.'), blank=True)

    exame_deformidades = models.TextField(verbose_name=_('Deformidades'), blank=True)
    exame_tonus = models.TextField(verbose_name=_('Tônus'), blank=True)
    exame_trofismo = models.TextField(verbose_name=_('Trofismo'), blank=True)
    exame_retracoes_encurtamento = models.TextField(verbose_name=_('Retrações ou Encurtamentos'), blank=True)

    reflexos_bicipital = models.CharField(max_length=40, verbose_name=_('Bicipital - C6'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_tricipital = models.CharField(max_length=40, verbose_name=_('Tricipital - C7'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_patelar = models.CharField(max_length=40, verbose_name=_('Patelar - L2, L3 e L4'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)
    reflexos_anquileu = models.CharField(max_length=40, verbose_name=_('Anquileu - L5, S1 e S2'), choices=[('Normoreflexia', 'Normoreflexia'), ('Hiporeflexia', 'Hiporeflexia'), ('Hiperreflexia', 'Hiperreflexia'), ('Arreflexia', 'Arreflexia')], blank=True)

    adm_ms = models.TextField(verbose_name=_('Membros Superiores'), blank=True)
    adm_mi = models.TextField(verbose_name=_('Membros Inferiores'), blank=True)
    adm_avd = models.CharField(max_length=40, verbose_name=_('AVD\'s'), choices=[('Independente', 'Independente'), ('Dependente', 'Dependente'), ('Semi-Independente', 'Semi-Independente')], blank=True)
    adm_marcha = models.CharField(max_length=40, verbose_name=_('Marcha'), blank=True)

    desenvolvimento_conduta = models.TextField(verbose_name=_('Conduta Fisioterapêutica'), blank=True)
    desenvolvimento_objetivo = models.TextField(verbose_name=_('Objetivos de Tratamento'), blank=True)

    atendimento_estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)
    atendimento_supervisor = models.CharField(max_length=40, verbose_name=_('Supervissor (a)'), blank=True)

    class Meta:
        verbose_name = _('Avaliação Neurológica')
        verbose_name_plural = _('Avaliações Neurológica')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaParkinson(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)

    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    diagnostico_clinico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Fisioterápico'), blank=True)

    dados_pa = models.CharField(max_length=40, verbose_name=_('P.A.'), blank=True)
    dados_fc = models.CharField(max_length=40, verbose_name=_('F.C.'), blank=True)
    dados_fr = models.CharField(max_length=40, verbose_name=_('F.R.'), blank=True)
    dados_t = models.CharField(max_length=40, verbose_name=_('T°'), blank=True)

    info_medicamentos = models.TextField(verbose_name=_('Medicamentos Utilizados'), blank=True)
    info_patologias = models.TextField(verbose_name=_('Patologias Associadas'), blank=True)
    info_antecedentes = models.TextField(verbose_name=_('Antecedentes Cirúrgicos'), blank=True)

    anamnese_qp = models.TextField(verbose_name=_('Q.P.'), blank=True)
    anamnese_hmpa = models.TextField(verbose_name=_('H.M.P.A.'), blank=True)

    exame_1 = models.CharField(
        max_length=10,
        verbose_name=_('Bradicinesia de Mãos - Incluindo Escrita Manual: '),
        default=0)

    exame_2 = models.CharField(
        max_length=10,
        verbose_name=_('Rigidez: '),
        default=0)

    exame_3 = models.CharField(
        max_length=10,
        verbose_name=_('Postura: '),
        default=0)

    exame_4 = models.CharField(
        max_length=10,
        verbose_name=_('Balanceio de Membros Superior: '),
        default=0)

    exame_5 = models.CharField(
        max_length=10,
        verbose_name=_('Marcha: '),
        default=0)

    exame_6 = models.CharField(
        max_length=10,
        verbose_name=_('Tremor: '),
        default=0)

    exame_7 = models.CharField(
        max_length=10,
        verbose_name=_('Face: '),
        default=0)

    exame_8 = models.CharField(
        max_length=10,
        verbose_name=_('Seborréia: '),
        default=0)

    exame_9 = models.CharField(
        max_length=10,
        verbose_name=_('Fala: '),
        default=0)

    exame_10 = models.CharField(
        max_length=10,
        verbose_name=_('Cuidados Pessoais: '),
        default=0)

    exame_total = models.CharField(max_length=40, verbose_name=_('Total'), blank=True)

    exame_adm = models.TextField(verbose_name=_('ADM'), blank=True)
    exame_trofismo = models.TextField(verbose_name=_('Trofismo'), blank=True)

    desenvolvimento_objetivo = models.TextField(verbose_name=_('Objetivos de Tratamento'), blank=True)
    desenvolvimento_conduta = models.TextField(verbose_name=_('Conduta Fisioterapêutica'), blank=True)
    desenvolvimento_complemento = models.TextField(verbose_name=_('Complementações'), blank=True)

    atendimento_estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)
    atendimento_supervisor = models.CharField(max_length=40, verbose_name=_('Supervissor (a)'), blank=True)


    class Meta:
        verbose_name = _('Avaliação Parkinson')
        verbose_name_plural = _('Avaliações Parkinson')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaParalisiaFacial(models.Model):
    data = models.DateField(verbose_name=_('Data da Avaliação'), blank=True)

    paciente = models.ForeignKey(Paciente, verbose_name=_('Nome'))
    data_nascimento = models.DateField(verbose_name=_('Data de Nascimento'), blank=True)
    idade = models.CharField(max_length=40, verbose_name=_('Idade'), blank=True)
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    endereco = models.CharField(max_length=40, verbose_name=_('Endereço'), blank=True)
    telefone = models.CharField(max_length=40, verbose_name=_('Telefone'), blank=True)
    profissao = models.CharField(max_length=40, verbose_name=_('Profissão'), blank=True)
    estado_civil = models.CharField(max_length=40, verbose_name=_('Estado Civil'), blank=True)
    diagnostico_clinico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Clínico'), blank=True)
    diagnostico_fisioterapico = models.CharField(max_length=40, verbose_name=_('Diagnóstico Fisioterápico'), blank=True)

    dados_pa = models.CharField(max_length=40, verbose_name=_('P.A.'), blank=True)
    dados_fc = models.CharField(max_length=40, verbose_name=_('F.C.'), blank=True)
    dados_fr = models.CharField(max_length=40, verbose_name=_('F.R.'), blank=True)
    dados_t = models.CharField(max_length=40, verbose_name=_('T°'), blank=True)

    info_medicamentos = models.TextField(verbose_name=_('Medicamentos Utilizados'), blank=True)
    info_patologias = models.TextField(verbose_name=_('Patologias Associadas'), blank=True)
    info_antecedentes = models.TextField(verbose_name=_('Antecedentes Cirúrgicos'), blank=True)

    anamnese_qp = models.TextField(verbose_name=_('Q.P.'), blank=True)
    anamnese_hmpa = models.TextField(verbose_name=_('H.M.P.A.'), blank=True)

    exame_desvio_facial = models.CharField(max_length=40, verbose_name=_('Desvio Facial'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_desvio_septo = models.CharField(max_length=40, verbose_name=_('Desvio do Septo Nasal'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_sulco_face = models.CharField(max_length=40, verbose_name=_('Sulcos da Face'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_conjuntivite = models.CharField(max_length=40, verbose_name=_('Conjuntivite'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_lagoftalmo = models.CharField(max_length=40, verbose_name=_('Lagoftalmo'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_sinal_bell = models.CharField(max_length=40, verbose_name=_('Sinal Bell'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_sinal_negro = models.CharField(max_length=40, verbose_name=_('Sinal Negro'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_reflexo_ciliar = models.CharField(max_length=40, verbose_name=_('Reflexo Ciliar'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente')), ('Retardado', _('Retardado'))], blank=True)
    exame_linguagem = models.CharField(max_length=40, verbose_name=_('Alterações da Linguagem (P-B-M)'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_auditiva = models.CharField(max_length=40, verbose_name=_('Alteração Auditiva'), choices=[('Hipoacusia', _('Hipoacusia')),( 'Hiperacusia', _('Hiperacusia')), ('Ausente', _('Ausente'))], blank=True)
    exame_gustativa = models.CharField(max_length=40, verbose_name=_('Alteração Gustativa'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_tonus = models.CharField(max_length=40, verbose_name=_('Tônus Muscular'), choices=[('Hipertônico', _('Hipertônico')), ('Hipotônico', _('Hipotônico')), ('Normal', _('Normal'))], blank=True)
    exame_dor = models.CharField(max_length=40, verbose_name=_('Dor Retroauricular'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_sincinesias = models.CharField(max_length=40, verbose_name=_('Sincinésias'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_lingua = models.CharField(max_length=40, verbose_name=_('Motricidade da Língua'), choices=[('Presente', _('Presente')), ('Ausente', _('Ausente'))], blank=True)
    exame_paralisia = models.CharField(max_length=40, verbose_name=_('Paralisia Facial Difinitiva'), choices=[('Central', _('Central')), ('Periférica', _('Periférica'))], blank=True)

    prova_musculos_esq_c = models.CharField(max_length=40, verbose_name=_('Músculos Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_musculos_esq_t = models.CharField(max_length=40, verbose_name=_('Músculos Esq. [T]'), choices=TONUS, blank=True)
    prova_musculos_esq_s = models.CharField(max_length=40, verbose_name=_('Músculos Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_musculos_dir_c = models.CharField(max_length=40, verbose_name=_('Músculos Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_musculos_dir_t = models.CharField(max_length=40, verbose_name=_('Músculos Dir. [T]'), choices=TONUS, blank=True)
    prova_musculos_dir_S = models.CharField(max_length=40, verbose_name=_('Músculos Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_musculares_esq_c = models.CharField(max_length=40, verbose_name=_('Porções Musculares Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_musculares_esq_t = models.CharField(max_length=40, verbose_name=_('Porções Musculares Esq. [T]'), choices=TONUS, blank=True)
    prova_musculares_esq_s = models.CharField(max_length=40, verbose_name=_('Porções Musculares Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_musculares_dir_c = models.CharField(max_length=40, verbose_name=_('Porções Musculares Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_musculares_dir_t = models.CharField(max_length=40, verbose_name=_('Porções Musculares Dir. [T]'), choices=TONUS, blank=True)
    prova_musculares_dir_S = models.CharField(max_length=40, verbose_name=_('Porções Musculares Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_frontal_esq_c = models.CharField(max_length=40, verbose_name=_('Frontal Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_frontal_esq_t = models.CharField(max_length=40, verbose_name=_('Frontal Esq. [T]'), choices=TONUS, blank=True)
    prova_frontal_esq_s = models.CharField(max_length=40, verbose_name=_('Frontal Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_frontal_dir_c = models.CharField(max_length=40, verbose_name=_('Frontal Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_frontal_dir_t = models.CharField(max_length=40, verbose_name=_('Frontal Dir. [T]'), choices=TONUS, blank=True)
    prova_frontal_dir_S = models.CharField(max_length=40, verbose_name=_('Frontal Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_testa_esq_c = models.CharField(max_length=40, verbose_name=_('Franzir a Testa Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_testa_esq_t = models.CharField(max_length=40, verbose_name=_('Franzir a Testa Esq. [T]'), choices=TONUS, blank=True)
    prova_testa_esq_s = models.CharField(max_length=40, verbose_name=_('Franzir a Testa Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_testa_dir_c = models.CharField(max_length=40, verbose_name=_('Franzir a Testa Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_testa_dir_t = models.CharField(max_length=40, verbose_name=_('Franzir a Testa Dir. [T]'), choices=TONUS, blank=True)
    prova_testa_dir_S = models.CharField(max_length=40, verbose_name=_('Franzir a Testa Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_superciliar_esq_c = models.CharField(max_length=40, verbose_name=_('Superciliar Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_superciliar_esq_t = models.CharField(max_length=40, verbose_name=_('Superciliar Esq. [T]'), choices=TONUS, blank=True)
    prova_superciliar_esq_s = models.CharField(max_length=40, verbose_name=_('Superciliar Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_superciliar_dir_c = models.CharField(max_length=40, verbose_name=_('Superciliar Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_superciliar_dir_t = models.CharField(max_length=40, verbose_name=_('Superciliar Dir. [T]'), choices=TONUS, blank=True)
    prova_superciliar_dir_S = models.CharField(max_length=40, verbose_name=_('Superciliar Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_supercilios_esq_c = models.CharField(max_length=40, verbose_name=_('Aproximar os Supercílios Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_supercilios_esq_t = models.CharField(max_length=40, verbose_name=_('Aproximar os Supercílios Esq. [T]'), choices=TONUS, blank=True)
    prova_supercilios_esq_s = models.CharField(max_length=40, verbose_name=_('Aproximar os Supercílios Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_supercilios_dir_c = models.CharField(max_length=40, verbose_name=_('Aproximar os Supercílios Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_supercilios_dir_t = models.CharField(max_length=40, verbose_name=_('Aproximar os Supercílios Dir. [T]'), choices=TONUS, blank=True)
    prova_supercilios_dir_S = models.CharField(max_length=40, verbose_name=_('Aproximar os Supercílios Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_palpebral_esq_c = models.CharField(max_length=40, verbose_name=_('Porção Palpebral Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_palpebral_esq_t = models.CharField(max_length=40, verbose_name=_('Porção Palpebral Esq. [T]'), choices=TONUS, blank=True)
    prova_palpebral_esq_s = models.CharField(max_length=40, verbose_name=_('Porção Palpebral Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_palpebral_dir_c = models.CharField(max_length=40, verbose_name=_('Porção Palpebral Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_palpebral_dir_t = models.CharField(max_length=40, verbose_name=_('Porção Palpebral Dir. [T]'), choices=TONUS, blank=True)
    prova_palpebral_dir_S = models.CharField(max_length=40, verbose_name=_('Porção Palpebral Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_olhos_devagar_esq_c = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos Devagar Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_olhos_devagar_esq_t = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos Devagar Esq. [T]'), choices=TONUS, blank=True)
    prova_olhos_devagar_esq_s = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos Devagar Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_olhos_devagar_dir_c = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos Devagar Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_olhos_devagar_dir_t = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos Devagar Dir. [T]'), choices=TONUS, blank=True)
    prova_olhos_devagar_dir_S = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos Devagar Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_orbitaria_esq_c = models.CharField(max_length=40, verbose_name=_('Porção Orbitária Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_orbitaria_esq_t = models.CharField(max_length=40, verbose_name=_('Porção Orbitária Esq. [T]'), choices=TONUS, blank=True)
    prova_orbitaria_esq_s = models.CharField(max_length=40, verbose_name=_('Porção Orbitária Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_orbitaria_dir_c = models.CharField(max_length=40, verbose_name=_('Porção Orbitária Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_orbitaria_dir_t = models.CharField(max_length=40, verbose_name=_('Porção Orbitária Dir. [T]'), choices=TONUS, blank=True)
    prova_orbitaria_dir_S = models.CharField(max_length=40, verbose_name=_('Porção Orbitária Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_olhos_forca_esq_c = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos com Força Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_olhos_forca_esq_t = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos com Força Esq. [T]'), choices=TONUS, blank=True)
    prova_olhos_forca_esq_s = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos com Força Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_olhos_forca_dir_c = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos com Força Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_olhos_forca_dir_t = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos com Força Dir. [T]'), choices=TONUS, blank=True)
    prova_olhos_forca_dir_S = models.CharField(max_length=40, verbose_name=_('Fechar os Olhos com Força Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_piramidal_esq_c = models.CharField(max_length=40, verbose_name=_('Piramidal Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_piramidal_esq_t = models.CharField(max_length=40, verbose_name=_('Piramidal Esq. [T]'), choices=TONUS, blank=True)
    prova_piramidal_esq_s = models.CharField(max_length=40, verbose_name=_('Piramidal Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_piramidal_dir_c = models.CharField(max_length=40, verbose_name=_('Piramidal Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_piramidal_dir_t = models.CharField(max_length=40, verbose_name=_('Piramidal Dir. [T]'), choices=TONUS, blank=True)
    prova_piramidal_dir_S = models.CharField(max_length=40, verbose_name=_('Piramidal Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_nariz_esq_c = models.CharField(max_length=40, verbose_name=_('Franzir o Nariz Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_nariz_esq_t = models.CharField(max_length=40, verbose_name=_('Franzir o Nariz Esq. [T]'), choices=TONUS, blank=True)
    prova_nariz_esq_s = models.CharField(max_length=40, verbose_name=_('Franzir o Nariz Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_nariz_dir_c = models.CharField(max_length=40, verbose_name=_('Franzir o Nariz Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_nariz_dir_t = models.CharField(max_length=40, verbose_name=_('Franzir o Nariz Dir. [T]'), choices=TONUS, blank=True)
    prova_nariz_dir_S = models.CharField(max_length=40, verbose_name=_('Franzir o Nariz Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_alar_esq_c = models.CharField(max_length=40, verbose_name=_('Porção Alar Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_alar_esq_t = models.CharField(max_length=40, verbose_name=_('Porção Alar Esq. [T]'), choices=TONUS, blank=True)
    prova_alar_esq_s = models.CharField(max_length=40, verbose_name=_('Porção Alar Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_alar_dir_c = models.CharField(max_length=40, verbose_name=_('Porção Alar Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_alar_dir_t = models.CharField(max_length=40, verbose_name=_('Porção Alar Dir. [T]'), choices=TONUS, blank=True)
    prova_alar_dir_S = models.CharField(max_length=40, verbose_name=_('Porção Alar Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_dilatar_narinas_esq_c = models.CharField(max_length=40, verbose_name=_('Dilatar as Narinas Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_dilatar_narinas_esq_t = models.CharField(max_length=40, verbose_name=_('Dilatar as Narinas Esq. [T]'), choices=TONUS, blank=True)
    prova_dilatar_narinas_esq_s = models.CharField(max_length=40, verbose_name=_('Dilatar as Narinas Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_dilatar_narinas_dir_c = models.CharField(max_length=40, verbose_name=_('Dilatar as Narinas Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_dilatar_narinas_dir_t = models.CharField(max_length=40, verbose_name=_('Dilatar as Narinas Dir. [T]'), choices=TONUS, blank=True)
    prova_dilatar_narinas_dir_S = models.CharField(max_length=40, verbose_name=_('Dilatar as Narinas Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_transversal_esq_c = models.CharField(max_length=40, verbose_name=_('Porção Transversal Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_transversal_esq_t = models.CharField(max_length=40, verbose_name=_('Porção Transversal Esq. [T]'), choices=TONUS, blank=True)
    prova_transversal_esq_s = models.CharField(max_length=40, verbose_name=_('Porção Transversal Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_transversal_dir_c = models.CharField(max_length=40, verbose_name=_('Porção Transversal Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_transversal_dir_t = models.CharField(max_length=40, verbose_name=_('Porção Transversal Dir. [T]'), choices=TONUS, blank=True)
    prova_transversal_dir_S = models.CharField(max_length=40, verbose_name=_('Porção Transversal Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_comprimir_narinas_esq_c = models.CharField(max_length=40, verbose_name=_('Comprimir as Narinas Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_comprimir_narinas_esq_t = models.CharField(max_length=40, verbose_name=_('Comprimir as Narinas Esq. [T]'), choices=TONUS, blank=True)
    prova_comprimir_narinas_esq_s = models.CharField(max_length=40, verbose_name=_('Comprimir as Narinas Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_comprimir_narinas_dir_c = models.CharField(max_length=40, verbose_name=_('Comprimir as Narinas Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_comprimir_narinas_dir_t = models.CharField(max_length=40, verbose_name=_('Comprimir as Narinas Dir. [T]'), choices=TONUS, blank=True)
    prova_comprimir_narinas_dir_S = models.CharField(max_length=40, verbose_name=_('Comprimir as Narinas Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_elevador_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Elevador do Lábio Superior e Zigomático Menor Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_elevador_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Elevador do Lábio Superior e Zigomático Menor Esq. [T]'), choices=TONUS, blank=True)
    prova_elevador_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Elevador do Lábio Superior e Zigomático Menor Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_elevador_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Elevador do Lábio Superior e Zigomático Menor Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_elevador_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Elevador do Lábio Superior e Zigomático Menor Dir. [T]'), choices=TONUS, blank=True)
    prova_elevador_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Elevador do Lábio Superior e Zigomático Menor Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_elevar_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Elevar o Lábio Superior Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_elevar_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Elevar o Lábio Superior Esq. [T]'), choices=TONUS, blank=True)
    prova_elevar_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Elevar o Lábio Superior Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_elevar_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Elevar o Lábio Superior Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_elevar_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Elevar o Lábio Superior Dir. [T]'), choices=TONUS, blank=True)
    prova_elevar_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Elevar o Lábio Superior Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_zigomatico_esq_c = models.CharField(max_length=40, verbose_name=_('Zigomático Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_zigomatico_esq_t = models.CharField(max_length=40, verbose_name=_('Zigomático Esq. [T]'), choices=TONUS, blank=True)
    prova_zigomatico_esq_s = models.CharField(max_length=40, verbose_name=_('Zigomático Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_zigomatico_dir_c = models.CharField(max_length=40, verbose_name=_('Zigomático Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_zigomatico_dir_t = models.CharField(max_length=40, verbose_name=_('Zigomático Dir. [T]'), choices=TONUS, blank=True)
    prova_zigomatico_dir_S = models.CharField(max_length=40, verbose_name=_('Zigomático Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_comissura_labial_esq_c = models.CharField(max_length=40, verbose_name=_('Elevar a Comissura Labial por Trás Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_comissura_labial_esq_t = models.CharField(max_length=40, verbose_name=_('Elevar a Comissura Labial por Trás Esq. [T]'), choices=TONUS, blank=True)
    prova_comissura_labial_esq_s = models.CharField(max_length=40, verbose_name=_('Elevar a Comissura Labial por Trás Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_comissura_labial_dir_c = models.CharField(max_length=40, verbose_name=_('Elevar a Comissura Labial por Trás Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_comissura_labial_dir_t = models.CharField(max_length=40, verbose_name=_('Elevar a Comissura Labial por Trás Dir. [T]'), choices=TONUS, blank=True)
    prova_comissura_labial_dir_S = models.CharField(max_length=40, verbose_name=_('Elevar a Comissura Labial por Trás Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_canino_esq_c = models.CharField(max_length=40, verbose_name=_('Canino Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_canino_esq_t = models.CharField(max_length=40, verbose_name=_('Canino Esq. [T]'), choices=TONUS, blank=True)
    prova_canino_esq_s = models.CharField(max_length=40, verbose_name=_('Canino Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_canino_dir_c = models.CharField(max_length=40, verbose_name=_('Canino Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_canino_dir_t = models.CharField(max_length=40, verbose_name=_('Canino Dir. [T]'), choices=TONUS, blank=True)
    prova_canino_dir_S = models.CharField(max_length=40, verbose_name=_('Canino Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_elevar_canto_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Elevar o Canto do Lábio Superior Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_elevar_canto_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Elevar o Canto do Lábio Superior Esq. [T]'), choices=TONUS, blank=True)
    prova_elevar_canto_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Elevar o Canto do Lábio Superior Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_elevar_canto_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Elevar o Canto do Lábio Superior Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_elevar_canto_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Elevar o Canto do Lábio Superior Dir. [T]'), choices=TONUS, blank=True)
    prova_elevar_canto_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Elevar o Canto do Lábio Superior Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_depressor_septo_esq_c = models.CharField(max_length=40, verbose_name=_('Depressor do Septo Nasal Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_depressor_septo_esq_t = models.CharField(max_length=40, verbose_name=_('Depressor do Septo Nasal Esq. [T]'), choices=TONUS, blank=True)
    prova_depressor_septo_esq_s = models.CharField(max_length=40, verbose_name=_('Depressor do Septo Nasal Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_depressor_septo_dir_c = models.CharField(max_length=40, verbose_name=_('Depressor do Septo Nasal Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_depressor_septo_dir_t = models.CharField(max_length=40, verbose_name=_('Depressor do Septo Nasal Dir. [T]'), choices=TONUS, blank=True)
    prova_depressor_septo_dir_S = models.CharField(max_length=40, verbose_name=_('Depressor do Septo Nasal Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_deprimir_septo_esq_c = models.CharField(max_length=40, verbose_name=_('Deprimir o Septo Nasal Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_deprimir_septo_esq_t = models.CharField(max_length=40, verbose_name=_('Deprimir o Septo Nasal Esq. [T]'), choices=TONUS, blank=True)
    prova_deprimir_septo_esq_s = models.CharField(max_length=40, verbose_name=_('Deprimir o Septo Nasal Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_deprimir_septo_dir_c = models.CharField(max_length=40, verbose_name=_('Deprimir o Septo Nasal Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_deprimir_septo_dir_t = models.CharField(max_length=40, verbose_name=_('Deprimir o Septo Nasal Dir. [T]'), choices=TONUS, blank=True)
    prova_deprimir_septo_dir_S = models.CharField(max_length=40, verbose_name=_('Deprimir o Septo Nasal Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_orbicular_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Obicular do Lábio Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_orbicular_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Obicular do Lábio Esq. [T]'), choices=TONUS, blank=True)
    prova_orbicular_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Obicular do Lábio Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_orbicular_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Obicular do Lábio Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_orbicular_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Obicular do Lábio Dir. [T]'), choices=TONUS, blank=True)
    prova_orbicular_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Obicular do Lábio Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_bico_esq_c = models.CharField(max_length=40, verbose_name=_('Fazer Bico Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_bico_esq_t = models.CharField(max_length=40, verbose_name=_('Fazer Bico Esq. [T]'), choices=TONUS, blank=True)
    prova_bico_esq_s = models.CharField(max_length=40, verbose_name=_('Fazer Bico Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_bico_dir_c = models.CharField(max_length=40, verbose_name=_('Fazer Bico Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_bico_dir_t = models.CharField(max_length=40, verbose_name=_('Fazer Bico Dir. [T]'), choices=TONUS, blank=True)
    prova_bico_dir_S = models.CharField(max_length=40, verbose_name=_('Fazer Bico Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_bucinador_esq_c = models.CharField(max_length=40, verbose_name=_('Bucinador Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_bucinador_esq_t = models.CharField(max_length=40, verbose_name=_('Bucinador Esq. [T]'), choices=TONUS, blank=True)
    prova_bucinador_esq_s = models.CharField(max_length=40, verbose_name=_('Bucinador Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_bucinador_dir_c = models.CharField(max_length=40, verbose_name=_('Bucinador Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_bucinador_dir_t = models.CharField(max_length=40, verbose_name=_('Bucinador Dir. [T]'), choices=TONUS, blank=True)
    prova_bucinador_dir_S = models.CharField(max_length=40, verbose_name=_('Bucinador Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_labio_bochecha_esq_c = models.CharField(max_length=40, verbose_name=_('Aproximar os Lábios e Comprimir as Bochechas Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_labio_bochecha_esq_t = models.CharField(max_length=40, verbose_name=_('Aproximar os Lábios e Comprimir as Bochechas Esq. [T]'), choices=TONUS, blank=True)
    prova_labio_bochecha_esq_s = models.CharField(max_length=40, verbose_name=_('Aproximar os Lábios e Comprimir as Bochechas Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_labio_bochecha_dir_c = models.CharField(max_length=40, verbose_name=_('Aproximar os Lábios e Comprimir as Bochechas Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_labio_bochecha_dir_t = models.CharField(max_length=40, verbose_name=_('Aproximar os Lábios e Comprimir as Bochechas Dir. [T]'), choices=TONUS, blank=True)
    prova_labio_bochecha_dir_S = models.CharField(max_length=40, verbose_name=_('Aproximar os Lábios e Comprimir as Bochechas Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_risorio_esq_c = models.CharField(max_length=40, verbose_name=_('Risório Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_risorio_esq_t = models.CharField(max_length=40, verbose_name=_('Risório Esq. [T]'), choices=TONUS, blank=True)
    prova_risorio_esq_s = models.CharField(max_length=40, verbose_name=_('Risório Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_risorio_dir_c = models.CharField(max_length=40, verbose_name=_('Risório Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_risorio_dir_t = models.CharField(max_length=40, verbose_name=_('Risório Dir. [T]'), choices=TONUS, blank=True)
    prova_risorio_dir_S = models.CharField(max_length=40, verbose_name=_('Risório Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_labio_fechado_esq_c = models.CharField(max_length=40, verbose_name=_('Lábios Fechados, Levar Canto da Boca P/ Lateral Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_labio_fechado_esq_t = models.CharField(max_length=40, verbose_name=_('Lábios Fechados, Levar Canto da Boca P/ Lateral Esq. [T]'), choices=TONUS, blank=True)
    prova_labio_fechado_esq_s = models.CharField(max_length=40, verbose_name=_('Lábios Fechados, Levar Canto da Boca P/ Lateral Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_labio_fechado_dir_c = models.CharField(max_length=40, verbose_name=_('Lábios Fechados, Levar Canto da Boca P/ Lateral Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_labio_fechado_dir_t = models.CharField(max_length=40, verbose_name=_('Lábios Fechados, Levar Canto da Boca P/ Lateral Dir. [T]'), choices=TONUS, blank=True)
    prova_labio_fechado_dir_S = models.CharField(max_length=40, verbose_name=_('Lábios Fechados, Levar Canto da Boca P/ Lateral Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_mento_esq_c = models.CharField(max_length=40, verbose_name=_('Quadrado do Mento Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_mento_esq_t = models.CharField(max_length=40, verbose_name=_('Quadrado do Mento Esq. [T]'), choices=TONUS, blank=True)
    prova_mento_esq_s = models.CharField(max_length=40, verbose_name=_('Quadrado do Mento Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_mento_dir_c = models.CharField(max_length=40, verbose_name=_('Quadrado do Mento Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_mento_dir_t = models.CharField(max_length=40, verbose_name=_('Quadrado do Mento Dir. [T]'), choices=TONUS, blank=True)
    prova_mento_dir_S = models.CharField(max_length=40, verbose_name=_('Quadrado do Mento Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_enrugar_mento_esq_c = models.CharField(max_length=40, verbose_name=_('Enrugar o Mento Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_enrugar_mento_esq_t = models.CharField(max_length=40, verbose_name=_('Enrugar o Mento Esq. [T]'), choices=TONUS, blank=True)
    prova_enrugar_mento_esq_s = models.CharField(max_length=40, verbose_name=_('Enrugar o Mento Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_enrugar_mento_dir_c = models.CharField(max_length=40, verbose_name=_('Enrugar o Mento Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_enrugar_mento_dir_t = models.CharField(max_length=40, verbose_name=_('Enrugar o Mento Dir. [T]'), choices=TONUS, blank=True)
    prova_enrugar_mento_dir_S = models.CharField(max_length=40, verbose_name=_('Enrugar o Mento Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_depresor_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Depressor do Lábio Inferior Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_depresor_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Depressor do Lábio Inferior Esq. [T]'), choices=TONUS, blank=True)
    prova_depresor_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Depressor do Lábio Inferior Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_depresor_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Depressor do Lábio Inferior Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_depresor_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Depressor do Lábio Inferior Dir. [T]'), choices=TONUS, blank=True)
    prova_depresor_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Depressor do Lábio Inferior Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_deprimir_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Deprimir Lábio Inferior, Ângulo da Boca P/ Baixo Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_deprimir_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Deprimir Lábio Inferior, Ângulo da Boca P/ Baixo Esq. [T]'), choices=TONUS, blank=True)
    prova_deprimir_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Deprimir Lábio Inferior, Ângulo da Boca P/ Baixo Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_deprimir_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Deprimir Lábio Inferior, Ângulo da Boca P/ Baixo Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_deprimir_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Deprimir Lábio Inferior, Ângulo da Boca P/ Baixo Dir. [T]'), choices=TONUS, blank=True)
    prova_deprimir_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Deprimir Lábio Inferior, Ângulo da Boca P/ Baixo Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_triangular_labio_esq_c = models.CharField(max_length=40, verbose_name=_('Triangular do Lábio Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_triangular_labio_esq_t = models.CharField(max_length=40, verbose_name=_('Triangular do Lábio Esq. [T]'), choices=TONUS, blank=True)
    prova_triangular_labio_esq_s = models.CharField(max_length=40, verbose_name=_('Triangular do Lábio Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_triangular_labio_dir_c = models.CharField(max_length=40, verbose_name=_('Triangular do Lábio Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_triangular_labio_dir_t = models.CharField(max_length=40, verbose_name=_('Triangular do Lábio Dir. [T]'), choices=TONUS, blank=True)
    prova_triangular_labio_dir_S = models.CharField(max_length=40, verbose_name=_('Triangular do Lábio Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_canto_boca_esq_c = models.CharField(max_length=40, verbose_name=_('Levar o Canto da Boca P/ Baixo Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_canto_boca_esq_t = models.CharField(max_length=40, verbose_name=_('Levar o Canto da Boca P/ Baixo Esq. [T]'), choices=TONUS, blank=True)
    prova_canto_boca_esq_s = models.CharField(max_length=40, verbose_name=_('Levar o Canto da Boca P/ Baixo Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_canto_boca_dir_c = models.CharField(max_length=40, verbose_name=_('Levar o Canto da Boca P/ Baixo Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_canto_boca_dir_t = models.CharField(max_length=40, verbose_name=_('Levar o Canto da Boca P/ Baixo Dir. [T]'), choices=TONUS, blank=True)
    prova_canto_boca_dir_S = models.CharField(max_length=40, verbose_name=_('Levar o Canto da Boca P/ Baixo Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_platisma_esq_c = models.CharField(max_length=40, verbose_name=_('Platisma Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_platisma_esq_t = models.CharField(max_length=40, verbose_name=_('Platisma Esq. [T]'), choices=TONUS, blank=True)
    prova_platisma_esq_s = models.CharField(max_length=40, verbose_name=_('Platisma Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_platisma_dir_c = models.CharField(max_length=40, verbose_name=_('Platisma Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_platisma_dir_t = models.CharField(max_length=40, verbose_name=_('Platisma Dir. [T]'), choices=TONUS, blank=True)
    prova_platisma_dir_S = models.CharField(max_length=40, verbose_name=_('Platisma Dir. [S]'), choices=SINSINESIAS, blank=True)

    prova_pescoco_esq_c = models.CharField(max_length=40, verbose_name=_('Contrair Pescoço Esq. [C]'), choices=CONTRACAO, blank=True)
    prova_pescoco_esq_t = models.CharField(max_length=40, verbose_name=_('Contrair Pescoço Esq. [T]'), choices=TONUS, blank=True)
    prova_pescoco_esq_s = models.CharField(max_length=40, verbose_name=_('Contrair Pescoço Esq. [S]'), choices=SINSINESIAS, blank=True)
    prova_pescoco_dir_c = models.CharField(max_length=40, verbose_name=_('Contrair Pescoço Dir. [C]'), choices=CONTRACAO, blank=True)
    prova_pescoco_dir_t = models.CharField(max_length=40, verbose_name=_('Contrair Pescoço Dir. [T]'), choices=TONUS, blank=True)
    prova_pescoco_dir_S = models.CharField(max_length=40, verbose_name=_('Contrair Pescoço Dir. [S]'), choices=SINSINESIAS, blank=True)

    desenvolvimento_conclusao = models.TextField(verbose_name=_('Conclusão da Prova de Função'), blank=True)
    desenvolvimento_objetivo = models.TextField(verbose_name=_('Objetivos do Tratamento'), blank=True)
    desenvolvimento_conduta = models.TextField(verbose_name=_('Conduta Fisioterápica'), blank=True)

    atendimento_estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)
    atendimento_supervisor = models.CharField(max_length=40, verbose_name=_('Supervissor (a)'), blank=True)


    class Meta:
        verbose_name = _('Avaliação Paralisia Facial')
        verbose_name_plural = _('Avaliações Paralisia Facial')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}


class FisioterapiaOrtopediaReavaliacao(models.Model):
    data = models.DateField(verbose_name=_('Data'), blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=_('Paciente'))
    estagiario = models.CharField(max_length=40, verbose_name=_('Estagiário (a)'), blank=True)

    # Exame Mecânico - Teste de Uma Repetição - Movimentos Ativos
    movimento_ativo_1 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [1]'), blank=True)
    movimento_ativo_1_eva = models.CharField(max_length=40, verbose_name=_('EVA [1]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_ativo_1_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [1]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    movimento_ativo_2 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [2]'), blank=True)
    movimento_ativo_2_eva = models.CharField(max_length=40, verbose_name=_('EVA [2]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_ativo_2_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [2]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    movimento_ativo_3 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [3]'), blank=True)
    movimento_ativo_3_eva = models.CharField(max_length=40, verbose_name=_('EVA [3]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_ativo_3_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [3]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    movimento_ativo_4 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [4]'), blank=True)
    movimento_ativo_4_eva = models.CharField(max_length=40, verbose_name=_('EVA [4]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_ativo_4_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [4]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    # Exame Mecânico - Teste de Uma Repetição - Movimentos Passivos
    movimento_passivo_1 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [1]'), blank=True)
    movimento_passivo_1_eva = models.CharField(max_length=40, verbose_name=_('EVA [1]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_passivo_1_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [1]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    movimento_passivo_2 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [2]'), blank=True)
    movimento_passivo_2_eva = models.CharField(max_length=40, verbose_name=_('EVA [2]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_passivo_2_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [2]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    movimento_passivo_3 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [3]'), blank=True)
    movimento_passivo_3_eva = models.CharField(max_length=40, verbose_name=_('EVA [3]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_passivo_3_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [3]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    movimento_passivo_4 = models.CharField(max_length=40, verbose_name=_('Movimento Realizado [4]'), blank=True)
    movimento_passivo_4_eva = models.CharField(max_length=40, verbose_name=_('EVA [4]'), blank=True, choices=[('Dor Durante o Movimento', _('Dor Durante o Movimento')), ('Dor no Final do Movimento', _('Dor no Final do Movimento'))])
    movimento_passivo_4_amplitude = models.CharField(max_length=40, verbose_name=_('Amplitude [4]'), blank=True, choices=[('Normal', _('Normal')), ('Reduzida', _('Reduzida'))])

    # Teste de 10 Repetições
    teste_repeticao_1 = models.TextField(verbose_name=_('Movimento ou postura realizados'), blank=True)
    teste_repeticao_2 = models.TextField(verbose_name=_('O que ocorreu com a dor durante o movimento? (Produz, abole, aumenta, diminui, nenhum efeito.)'), blank=True)
    teste_repeticao_3 = models.TextField(verbose_name=_('O que ocorreu com a dor após o movimento? (Melhor, pior, não melhor, não pior, nenhum efeito)'), blank=True)
    teste_repeticao_4 = models.TextField(verbose_name=_('O que ocorreu com a amplitude de movimento? (Aumento, diminuiu, nenhum efeito.)'), blank=True)

    diagnostico_fisioterapeutico = models.TextField(verbose_name=_('Diagnóstico Fisioterapeutico'), blank=True)

    objetivo_dor = models.CharField(max_length=40, verbose_name=_('Abolir a Dor'), blank=True, choices=YES_NO_CHOICES)
    objetivo_tonus = models.CharField(max_length=40, verbose_name=_('Normalizar Tônus'), blank=True, choices=YES_NO_CHOICES)
    objetivo_propriocepcao = models.CharField(max_length=40, verbose_name=_('Normalizar Propriocepção'), blank=True, choices=YES_NO_CHOICES)
    objetivo_marcha = models.CharField(max_length=40, verbose_name=_('Normalizar Marcha'), blank=True, choices=YES_NO_CHOICES)
    objetivo_adm = models.CharField(max_length=40, verbose_name=_('Normalizar Adm\'s'), blank=True, choices=YES_NO_CHOICES)
    objetivo_sensibilidade = models.CharField(max_length=40, verbose_name=_('Estimular Sensibilidade'), blank=True, choices=YES_NO_CHOICES)
    objetivo_inflamacao = models.CharField(max_length=40, verbose_name=_('Abolir Inflamação'), blank=True, choices=YES_NO_CHOICES)
    objetivo_aderencia = models.CharField(max_length=40, verbose_name=_('Liberar Aderências'), blank=True, choices=YES_NO_CHOICES)
    objetivo_fortalecer_musculatura = models.CharField(max_length=40, verbose_name=_('Fortalecer Musculatura'), blank=True, choices=YES_NO_CHOICES)
    objetivo_trofismo = models.CharField(max_length=40, verbose_name=_('Normalizar Trofismo'), blank=True, choices=YES_NO_CHOICES)
    objetivo_alongar_musculatura = models.CharField(max_length=40, verbose_name=_('Alongar Musculatura'), blank=True, choices=YES_NO_CHOICES)
    objetivo_edema = models.CharField(max_length=40, verbose_name=_('Abolir Edema'), blank=True, choices=YES_NO_CHOICES)
    objetivo_avd = models.CharField(max_length=40, verbose_name=_('Normalizar Avd\'s'), blank=True, choices=YES_NO_CHOICES)
    objetivo_postura = models.CharField(max_length=40, verbose_name=_('Corrigir Postura'), blank=True, choices=YES_NO_CHOICES)

    proposta_crioterapia = models.CharField(max_length=40, verbose_name=_('Crioterapia'), blank=True, choices=YES_NO_CHOICES)
    proposta_ultra_som = models.CharField(max_length=40, verbose_name=_('Ultra Som'), blank=True, choices=YES_NO_CHOICES)
    proposta_microondas = models.CharField(max_length=40, verbose_name=_('Microondas'), blank=True, choices=YES_NO_CHOICES)
    proposta_ondas_curtas = models.CharField(max_length=40, verbose_name=_('Ondas Curtas'), blank=True, choices=YES_NO_CHOICES)
    proposta_infravermelho = models.CharField(max_length=40, verbose_name=_('Infravermelho'), blank=True, choices=YES_NO_CHOICES)
    proposta_laser = models.CharField(max_length=40, verbose_name=_('Laser'), blank=True, choices=YES_NO_CHOICES)
    proposta_tens = models.CharField(max_length=40, verbose_name=_('T.E.N.S.'), blank=True, choices=YES_NO_CHOICES)
    proposta_interferencial = models.CharField(max_length=40, verbose_name=_('Interferencial'), blank=True, choices=YES_NO_CHOICES)
    proposta_fes = models.CharField(max_length=40, verbose_name=_('FES'), blank=True, choices=YES_NO_CHOICES)
    proposta_russa = models.CharField(max_length=40, verbose_name=_('Russa'), blank=True, choices=YES_NO_CHOICES)
    proposta_diadinamica = models.CharField(max_length=40, verbose_name=_('Diadinâmica'), blank=True, choices=YES_NO_CHOICES)
    proposta_turbilhao = models.CharField(max_length=40, verbose_name=_('Turbilhão'), blank=True, choices=YES_NO_CHOICES)
    proposta_contraste = models.CharField(max_length=40, verbose_name=_('Contraste'), blank=True, choices=YES_NO_CHOICES)
    proposta_outras = models.TextField(verbose_name=_('Outros'), blank=True)

    class Meta:
        verbose_name = _('Ficha de Reavaliação')
        verbose_name_plural = _('Fichas de Reavaliação')
        ordering = ['data']

    def __str__(self):
        return _('%(data)s') % {'data': self.data.strftime('%d/%m/%Y')}
