from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from utils import YES_NO_CHOICES, get_or_create_grupo, ESCALA_FUNCIONAL_BERG

from .models import Atendente, Coordenador, FisioterapiaBerg


class FisioterapiaBergForm(ModelForm):
    berg_1 = forms.ChoiceField(
        label=_('1. Posição sentada para posição em pé: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[1])

    berg_2 = forms.ChoiceField(
        label=_('2. Permanecer em pé sem apoio: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[2])

    berg_3 = forms.ChoiceField(
        label=_('3. Permanecer sentado sem apoio nas costas, mas com os pés apoiados no chão ou num banquinho: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[3])

    berg_4 = forms.ChoiceField(
        label=_('4. Posição em pé para posição sentada: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[4])

    berg_5 = forms.ChoiceField(
        label=_('5. Transferências: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[5])

    berg_6 = forms.ChoiceField(
        label=_('6. Permanecer em pé sem apoio com os olhos fechados: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[6])

    berg_7 = forms.ChoiceField(
        label=_('7. Permanecer em pé sem apoio com os pés juntos: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[7])

    berg_8 = forms.ChoiceField(
        label=_('8. Alcançar a frente com o braço estendido permanecendo em pé: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[8])

    berg_9 = forms.ChoiceField(
        label=_('9. Pegar um objeto do chão a partir de uma posição em pé: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[9])

    berg_10 = forms.ChoiceField(
        label=_('10. Virar-se e olhar para trás por cima dos ombros direito e esquerdo enquanto permanece em pé: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[10])

    berg_11 = forms.ChoiceField(
        label=_('11. Girar-se 360 graus: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[11])

    berg_12 = forms.ChoiceField(
        label=_('12. Posicionar os pés alternadamente no degrau ou banquinho enquanto permanece em pé sem apoio: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[12])

    berg_13 = forms.ChoiceField(
        label=_('13. Permanecer em pé sem apoio com um pé à frente: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[13])

    berg_14 = forms.ChoiceField(
        label=_('14. Permanecer em pé sobre uma perna: '),
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'Radio'}),
        choices=ESCALA_FUNCIONAL_BERG[14])

    class Meta:
        model = FisioterapiaBerg
        fields = '__all__'


class CoordenadorForm(ModelForm):

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
        model = Coordenador
        fields = ['nome', 'sexo', 'setor', 'telefone',
                  'celular', 'username', 'email', 'matricula']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(CoordenadorForm, self).__init__(*args, **kwargs)

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
        coordenador = super(CoordenadorForm, self).save(commit)

        # Cria User
        u = User.objects.create(username=coordenador.username, email=coordenador.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        u.groups.add(get_or_create_grupo('Coordenador'))
        u.save()

        coordenador.user = u
        coordenador.save()
        return coordenador

class CoordenadorEditForm(ModelForm):

    class Meta:
        model = Coordenador
        fields = ['nome', 'sexo', 'setor', 'telefone',
                  'celular', 'username', 'email', 'matricula']

        widgets = {'username': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'email': forms.TextInput(
                                 attrs={'style': 'text-transform:lowercase;'}),
                   }

    def __init__(self, *args, **kwargs):
        super(CoordenadorEditForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    @transaction.atomic
    def save(self, commit=False):
        coordenador = super(CoordenadorEditForm, self).save(commit)

        # User
        u = coordenador.user
        u.email = coordenador.email
        u.save()

        coordenador.save()
        return coordenador

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

class AtendenteForm(ModelForm):

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
        model = Atendente
        fields = ['nome', 'sexo', 'disciplina', 'telefone',
                  'celular', 'username', 'email', 'matricula',
                  'orientador', 'coorientador']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(AtendenteForm, self).__init__(*args, **kwargs)

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
        atendente = super(AtendenteForm, self).save(commit)

        # Cria User
        u = User.objects.create(username=atendente.username, email=atendente.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        u.groups.add(get_or_create_grupo('Atendente'))
        u.save()

        atendente.user = u
        atendente.save()
        return atendente

class AtendenteEditForm(ModelForm):

    class Meta:
        model = Atendente
        fields = ['nome', 'sexo', 'disciplina', 'telefone',
                  'celular', 'username', 'email', 'matricula',
                  'orientador', 'coorientador']

        widgets = {'username': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'email': forms.TextInput(
                                 attrs={'style': 'text-transform:lowercase;'}),
                   }

    def __init__(self, *args, **kwargs):
        super(AtendenteEditForm, self).__init__(*args, **kwargs)

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    @transaction.atomic
    def save(self, commit=False):
        atendente = super(AtendenteEditForm, self).save(commit)

        # User
        u = atendente.user
        u.email = atendente.email
        u.save()

        atendente.save()
        return atendente
