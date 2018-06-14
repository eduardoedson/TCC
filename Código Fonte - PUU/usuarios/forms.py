from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from utils import (AVALIACAO_PARKINSON, ESCALA_FUNCIONAL_BERG, YES_NO_CHOICES,
                   get_or_create_grupo)

from .models import (Aluno, FisioterapiaBerg, FisioterapiaParkinson,
                     Recepcionista, Supervisor)


class FisioterapiaBergForm(ModelForm):
    berg_1 = forms.ChoiceField(
        label=_('1. Posição sentada para posição em pé:<br />Instruções: Por favor, levante-se. Tente não usar suas mãos para se apoiar.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[1])

    berg_2 = forms.ChoiceField(
        label=_('2. Permanecer em pé sem apoio:<br />Instruções: Por favor, fique em pé por 2 minutos sem se apoiar.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[2])

    berg_3 = forms.ChoiceField(
        label=_('3. Permanecer sentado sem apoio nas costas, mas com os pés apoiados no chão ou num banquinho:<br />Instruções: Por favor, fique sentado sem apoiar as costas com os braços cruzados por 2 minutos.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[3])

    berg_4 = forms.ChoiceField(
        label=_('4. Posição em pé para posição sentada:<br />Instruções: Por favor, sente-se.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[4])

    berg_5 = forms.ChoiceField(
        label=_('5. Transferências:<br />Instruções: Arrume as cadeiras perpendicularmente ou uma de frente para a outra para uma transferência em pivô. Peça ao paciente para transferir-se de uma cadeira com apoio de braço para uma cadeira sem apoio de braço, e vice-versa. Você poderá utilizar duas cadeiras (uma com e outra sem apoio de braço) ou uma cama e uma cadeira.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[5])

    berg_6 = forms.ChoiceField(
        label=_('6. Permanecer em pé sem apoio com os olhos fechados:<br />Instruções: Por favor, fique em pé e feche os olhos por 10 segundos.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[6])

    berg_7 = forms.ChoiceField(
        label=_('7. Permanecer em pé sem apoio com os pés juntos:<br />Instruções: Junte seus pés e fique em pé sem se apoiar.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[7])

    berg_8 = forms.ChoiceField(
        label=_('8. Alcançar a frente com o braço estendido permanecendo em pé:<br />Instruções: Levante o braço a 90º. Estique os dedos e tente alcançar a frente o mais longe possível. (O examinador posiciona a régua no fim da ponta dos dedos quando o braço estiver a 90º. Ao serem esticados para frente, os dedos não devem tocar a régua. A medida a ser registrada é a distância que os dedos conseguem alcançar quando o paciente se inclina para frente o máximo que ele consegue. Quando possível, peça ao paciente para usar ambos os braços para evitar rotação do tronco).'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[8])

    berg_9 = forms.ChoiceField(
        label=_('9. Pegar um objeto do chão a partir de uma posição em pé:<br />Instruções: Pegue o sapato/chinelo que está na frente dos seus pés.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[9])

    berg_10 = forms.ChoiceField(
        label=_('10. Virar-se e olhar para trás por cima dos ombros direito e esquerdo enquanto permanece em pé:<br />Instruções: Vire-se para olhar diretamente atrás de você por cima do seu ombro esquerdo sem tirar os pés do chão. Faça o mesmo por cima do ombro direito. (O examinador poderá pegar um objeto e posicioná-lo diretamente atrás do paciente para estimular o movimento).'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[10])

    berg_11 = forms.ChoiceField(
        label=_('11. Girar-se 360 graus:<br />Instruções: Gire-se completamente ao redor de si mesmo. Pausa. Gire-se completamente ao redor de si mesmo em sentido contrário.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[11])

    berg_12 = forms.ChoiceField(
        label=_('12. Posicionar os pés alternadamente no degrau ou banquinho enquanto permanece em pé sem apoio:<br />Instruções: Toque cada pé alternadamente no degrau/banquinho. Continue até que cada pé tenha tocado o degrau/banquinho quatro vezes.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[12])

    berg_13 = forms.ChoiceField(
        label=_('13. Permanecer em pé sem apoio com um pé à frente:<br />Instruções: (demonstre para o paciente) Coloque um pé diretamente à frente do outro na mesma linha; se você achar que não irá conseguir, coloque o pé um pouco mais à frente do outro pé e levemente para o lado.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[13])

    berg_14 = forms.ChoiceField(
        label=_('14. Permanecer em pé sobre uma perna:<br />Instruções: Fique em pé sobre uma perna o máximo que você puder sem se segurar.'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[14])

    class Meta:
        model = FisioterapiaBerg
        fields = '__all__'


class SupervisorForm(ModelForm):

    # Usuário
    password = forms.CharField(
        max_length=20,
        label=_('Senha'),
        widget=forms.PasswordInput())

    password_confirm = forms.CharField(
        max_length=20,
        label=_('Confirmar Senha'),
        widget=forms.PasswordInput())

    class Meta:
        model = Supervisor
        fields = ['nome', 'sexo', 'setor', 'telefone',
                  'celular', 'username', 'email', 'matricula']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(SupervisorForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    def clean(self):

        if ('password' not in self.cleaned_data or
                'password_confirm' not in self.cleaned_data):
            raise ValidationError(_('Favor informar senhas atuais ou novas'))

        msg = _('As senhas não conferem.')
        self.valida_igualdade(
            self.cleaned_data['password'],
            self.cleaned_data['password_confirm'],
            msg)

        try:
            validate_password(self.cleaned_data['password'])
        except ValidationError as error:
            raise ValidationError(error)

        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=False):
        supervisor = super(SupervisorForm, self).save(commit)

        # Cria User
        u = User.objects.create(username=supervisor.username, email=supervisor.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        u.groups.add(get_or_create_grupo('Supervisor'))
        u.save()

        supervisor.user = u
        supervisor.save()
        return supervisor

class SupervisorEditForm(ModelForm):

    class Meta:
        model = Supervisor
        fields = ['nome', 'sexo', 'setor', 'telefone',
                  'celular', 'username', 'email', 'matricula']

        widgets = {'username': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'email': forms.TextInput(
                                 attrs={'style': 'text-transform:lowercase;'}),
                   }

    def __init__(self, *args, **kwargs):
        super(SupervisorEditForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    @transaction.atomic
    def save(self, commit=False):
        supervisor = super(SupervisorEditForm, self).save(commit)

        # User
        u = supervisor.user
        u.email = supervisor.email
        u.save()

        supervisor.save()
        return supervisor

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário", max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg',
                   'name': 'username',
                   'placeholder': 'Usuário'}))

    password = forms.CharField(
        label="Senha", max_length=30,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'name': 'password',
                   'placeholder': 'Senha'}))

class MudarSenhaForm(forms.Form):
    nova_senha = forms.CharField(
        label="Nova Senha", max_length=30,
        widget=forms.PasswordInput(
          attrs={'class': 'form-control form-control-lg',
                 'name': 'senha',
                 'placeholder': 'Nova Senha'}))

    confirmar_senha = forms.CharField(
        label="Confirmar Senha", max_length=30,
        widget=forms.PasswordInput(
          attrs={'class': 'form-control form-control-lg',
                 'name': 'confirmar_senha',
                 'placeholder': 'Confirmar Senha'}))

class AlunoForm(ModelForm):

    # Usuário
    password = forms.CharField(
        max_length=20,
        label=_('Senha'),
        widget=forms.PasswordInput())

    password_confirm = forms.CharField(
        max_length=20,
        label=_('Confirmar Senha'),
        widget=forms.PasswordInput())

    class Meta:
        model = Aluno
        fields = ['nome', 'sexo', 'disciplina', 'telefone',
                  'celular', 'username', 'email', 'matricula',
                  'supervisor']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    def clean(self):

        if ('password' not in self.cleaned_data or
                'password_confirm' not in self.cleaned_data):
            raise ValidationError(_('Favor informar senhas atuais ou novas'))

        msg = _('As senhas não conferem.')
        self.valida_igualdade(
            self.cleaned_data['password'],
            self.cleaned_data['password_confirm'],
            msg)

        try:
            validate_password(self.cleaned_data['password'])
        except ValidationError as error:
            raise ValidationError(error)

        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=False):
        aluno = super(AlunoForm, self).save(commit)

        # Cria User
        u = User.objects.create(username=aluno.username, email=aluno.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        u.groups.add(get_or_create_grupo('Aluno'))
        u.save()

        aluno.user = u
        aluno.save()
        return aluno

class AlunoEditForm(ModelForm):

    class Meta:
        model = Aluno
        fields = ['nome', 'sexo', 'disciplina', 'telefone',
                  'celular', 'username', 'email', 'matricula',
                  'supervisor']

        widgets = {'username': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'email': forms.TextInput(
                                 attrs={'style': 'text-transform:lowercase;'}),
                   }

    def __init__(self, *args, **kwargs):
        super(AlunoEditForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    @transaction.atomic
    def save(self, commit=False):
        aluno = super(AlunoEditForm, self).save(commit)

        # User
        u = aluno.user
        u.email = aluno.email
        u.save()

        aluno.save()
        return aluno


class RecepcionistaForm(ModelForm):

    # Usuário
    password = forms.CharField(
        max_length=20,
        label=_('Senha'),
        widget=forms.PasswordInput())

    password_confirm = forms.CharField(
        max_length=20,
        label=_('Confirmar Senha'),
        widget=forms.PasswordInput())

    class Meta:
        model = Recepcionista
        fields = ['nome', 'sexo', 'setor', 'username', 'email']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(RecepcionistaForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    def clean(self):

        if ('password' not in self.cleaned_data or
                'password_confirm' not in self.cleaned_data):
            raise ValidationError(_('Favor informar senhas atuais ou novas'))

        msg = _('As senhas não conferem.')
        self.valida_igualdade(
            self.cleaned_data['password'],
            self.cleaned_data['password_confirm'],
            msg)

        try:
            validate_password(self.cleaned_data['password'])
        except ValidationError as error:
            raise ValidationError(error)

        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=False):
        recepcionista = super(RecepcionistaForm, self).save(commit)

        # Cria User
        u = User.objects.create(username=recepcionista.username, email=recepcionista.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        u.groups.add(get_or_create_grupo('Recepcionista'))
        u.save()

        recepcionista.user = u
        recepcionista.save()
        return recepcionista

class RecepcionistaEditForm(ModelForm):

    class Meta:
        model = Recepcionista
        fields = ['nome', 'sexo', 'setor', 'username', 'email']

        widgets = {'username': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'email': forms.TextInput(
                                 attrs={'style': 'text-transform:lowercase;'}),
                   }

    def __init__(self, *args, **kwargs):
        super(RecepcionistaEditForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    @transaction.atomic
    def save(self, commit=False):
        recepcionista = super(RecepcionistaEditForm, self).save(commit)

        # User
        u = recepcionista.user
        u.email = recepcionista.email
        u.save()

        recepcionista.save()
        return recepcionista

class FisioterapiaParkinsonForm(ModelForm):
    exame_1 = forms.ChoiceField(
        label=_('Bradicinesia de Mãos - Incluindo Escrita Manual:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[1])

    exame_2 = forms.ChoiceField(
        label=_('Rigidez:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[2])

    exame_3 = forms.ChoiceField(
        label=_('Postura:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[3])

    exame_4 = forms.ChoiceField(
        label=_('Balanceio de Membros Superior:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[4])

    exame_5 = forms.ChoiceField(
        label=_('Marcha:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[5])

    exame_6 = forms.ChoiceField(
        label=_('Tremor:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[6])

    exame_7 = forms.ChoiceField(
        label=_('Face:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[7])

    exame_8 = forms.ChoiceField(
        label=_('Seborréia:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[8])

    exame_9 = forms.ChoiceField(
        label=_('Fala:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[9])

    exame_10 = forms.ChoiceField(
        label=_('Cuidados Pessoais:'),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=AVALIACAO_PARKINSON[10])

    class Meta:
        model = FisioterapiaParkinson
        fields = '__all__'
