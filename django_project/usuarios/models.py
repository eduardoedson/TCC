from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from servicos.models import Disciplina, Setor, AreaAtendimento
from utils import RANGE_SEXO, YES_NO_CHOICES, ESCALA_FUNCIONAL_BERG


def media_path(instance, filename):
    dir = _('./prontuario/%(nome)s/%(especialidade)s/%(data)s/%(arq)s') % {
        'nome' : instance.paciente.nome,
        'especialidade' : instance.especialidade,
        'data' : instance.data.strftime('%d-%m-%Y'),
        'arq' : filename
    }
    return dir

class Coordenador(models.Model):
    nome = models.CharField(max_length=80, verbose_name=_('Nome Completo'))
    sexo = models.CharField(max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    setor = models.ForeignKey(Setor, verbose_name=_('Setor Responsável'))
    matricula = models.CharField(max_length=13, blank=True, null=True, verbose_name=_('Matrícula'))

    telefone = models.CharField(max_length=14, blank=True, null=True, verbose_name=_('Telefone'))
    celular = models.CharField(max_length=15, verbose_name=_('Celular'))

    # Dados para logar no sistema
    user = models.ForeignKey(User)
    email = email = models.EmailField(unique=True, verbose_name=_('Email'))
    username = models.CharField(verbose_name=_('Nome de Usuário'), unique=True, max_length=30)

    class Meta:
        verbose_name = _('Coordenador (a)')
        verbose_name_plural = _('Coordenadores (as)')
        ordering = ['nome', 'setor']

    def __str__(self):
        return _('%(nome)s (%(setor)s)') % {
            'nome': self.nome, 'setor': self.setor.descricao}


class Atendente(models.Model):
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

    orientador = models.ForeignKey(Coordenador, verbose_name=_('Orientador'), related_name=_('orientador'))
    coorientador = models.ForeignKey(Coordenador, blank=True, null=True, verbose_name=_('Co-Orientador'), related_name=_('coorientador'))

    class Meta:
        verbose_name = _('Atendente')
        verbose_name_plural = _('Atendentes')
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
        choices=YES_NO_CHOICES, blank=True)
    atividade_fisica = models.CharField(
        max_length=10,
        verbose_name=_('Pratica atividade física?'),
        choices=YES_NO_CHOICES, blank=True)
    atividade_laboral = models.CharField(
        max_length=10,
        verbose_name=_('Pratica atividade laboral?'),
        choices=YES_NO_CHOICES, blank=True)

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

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name=_('Paciente'))
    medico = models.CharField(max_length=50, verbose_name=_('Médico'))
    especialidade = models.CharField(max_length=50, verbose_name=_('Especialidade'))
    descricao = models.TextField(verbose_name=_('Descrição'))
    data = models.DateField(verbose_name=_('Data Consulta'))
    hora = models.CharField(max_length=5, verbose_name=_('Hora Consulta'))
    arq_1 = models.FileField(
        blank=True, upload_to=media_path, verbose_name=_('Arquivo 1'))
    arq_2 = models.FileField(
        blank=True, upload_to=media_path, verbose_name=_('Arquivo 2'))

    class Meta:
        verbose_name = _('Prontuário')
        verbose_name_plural = _('Prontuários')
        ordering = ['paciente', 'data', 'hora', 'especialidade']

    def __str__(self):
        return _('%(paciente)s (%(data)s)') % {
            'paciente': self.paciente, 'data': self.data.strftime('%d/%m/%Y')}

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

    medicamento = models.CharField(max_length=20, verbose_name=_('Faz uso de medicamentos?'), choices=YES_NO_CHOICES, blank=True)
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

    estagiario = models.ForeignKey(Atendente, verbose_name=_('Estagiário'))
    supervisor = models.ForeignKey(Coordenador, verbose_name=_('Supervisor'))

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