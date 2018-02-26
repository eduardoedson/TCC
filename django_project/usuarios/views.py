from datetime import datetime

from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView

import crud.base
from crud.base import Crud
from prontuario.settings import LOGIN_REDIRECT_URL
from utils import lista_grupos, valida_igualdade

from .forms import (AlunoEditForm, AlunoForm, FisioterapiaBergForm,
                    FisioterapiaParkinsonForm, MudarSenhaForm,
                    RecepcionistaEditForm, RecepcionistaForm,
                    SupervisorEditForm, SupervisorForm)
from .models import (Aluno, FisioterapiaAcidenteVascularEncefalico,
                     FisioterapiaAvaliacaoFeminina,
                     FisioterapiaAvaliacaoGestacional,
                     FisioterapiaAvaliacaoMasculina, FisioterapiaBerg,
                     FisioterapiaEscleroseMultipla, FisioterapiaEvolucao,
                     FisioterapiaGeriatriaAnamnese,
                     FisioterapiaGeriatriaAvalicao,
                     FisioterapiaNeurologiaInfantilAvalicao,
                     FisioterapiaNeurologica, FisioterapiaOrtopediaAvaliacao,
                     FisioterapiaOrtopediaReavaliacao,
                     FisioterapiaParalisiaFacial, FisioterapiaParkinson,
                     FisioterapiaTriagem, FisioterapiaTRM, Paciente,
                     Recepcionista, Supervisor)


def get_medico(pk):
    try:
        supervisor = Supervisor.objects.get(user_id=pk)
    except ObjectDoesNotExist:
        try:
            aluno = Aluno.objects.get(user_id=pk)
        except ObjectDoesNotExist:
            return 0
        else:
            return [aluno, aluno.disciplina.setor.descricao]
    else:
        return [supervisor, supervisor.setor.descricao]


class FisioterapiaGeriatriaAnamneseCrud(Crud):
    model = FisioterapiaGeriatriaAnamnese
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Ficha de Avaliação / Anamnese'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaGeriatriaAnamnese.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiageriatriaanamnese_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['sexo'] = paciente.sexo
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaBergCrud(Crud):
    model = FisioterapiaBerg
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data', 'berg_total']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Escala de Equilíbrio Funcional de Berg'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaBerg.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):
        form_class = FisioterapiaBergForm

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaberg_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            self.initial['paciente'] = self.kwargs['pk']
            return self.initial.copy()

    class UpdateView(crud.base.CrudUpdateView):
        form_class = FisioterapiaBergForm

class FisioterapiaGeriatriaAvalicaoCrud(Crud):
    model = FisioterapiaGeriatriaAvalicao
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data_avaliacao', 'estagiario']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação de Geriatria'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaGeriatriaAvalicao.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiageriatriaavalicao_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            triagem = FisioterapiaTriagem.objects.filter(
                paciente_id=self.kwargs['pk']).last()
            paciente = Paciente.objects.get(id=self.kwargs['pk'])

            self.initial['data_nascimento'] = paciente.data_nascimento.strftime('%d/%m/%Y')
            self.initial['sexo'] = paciente.sexo
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['diagnostico_clinico'] = triagem.diagnostico if triagem else ''

            return self.initial.copy()

class FisioterapiaNeurologiaInfantilAvalicaoCrud(Crud):
    model = FisioterapiaNeurologiaInfantilAvalicao
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Fisioterápica em Neuropediatria'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaNeurologiaInfantilAvalicao.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse(
                'usuarios:fisioterapianeurologiainfantilavalicao_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            triagem = FisioterapiaTriagem.objects.filter(
                paciente_id=self.kwargs['pk']).last()

            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['diagnostico'] = triagem.diagnostico if triagem else ''
            self.initial['queixa_principal'] = triagem.queixa_principal if triagem else ''

            return self.initial.copy()


class FisioterapiaEvolucaoCrud(Crud):
    model = FisioterapiaEvolucao
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Evolução de Fisioterapia'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaEvolucao.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaevolucao_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            self.initial['paciente'] = self.kwargs['pk']
            return self.initial.copy()


class FisioterapiaTriagemCrud(Crud):
    model = FisioterapiaTriagem
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data_triagem', 'area_atendimento']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Triagem de Fisioterapia'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaTriagem.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiatriagem_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            self.initial['data_laudo'] = datetime.now().strftime('%d/%m/%Y')
            self.initial['paciente'] = self.kwargs['pk']
            return self.initial.copy()


class PacienteCrud(Crud):
    model = Paciente
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['nome', 'cpf', 'rg', 'data_nascimento']


def mudar_senha(request):

    if not request.user.is_authenticated():
        return render(request, '403.html', {})

    if request.method == 'GET':
        context = {'form': MudarSenhaForm}
        return render(request, 'mudar_senha.html', context)

    elif request.method == 'POST':
        form = MudarSenhaForm(request.POST)
        if form.is_valid():
            if (not valida_igualdade(form.cleaned_data['nova_senha'],
                                     form.cleaned_data['confirmar_senha'])):
                context = {'form': MudarSenhaForm,
                           'msg': 'As senhas não conferem.'}
                return render(request, 'mudar_senha.html', context)
            else:
                user = User.objects.get(id=request.user.id)
                user.set_password(form.cleaned_data['nova_senha'])
                user.save()
            return render(request, 'index.html', {'msg': 'Senha alterada.'})
        else:
            context = {'form': MudarSenhaForm,
                       'msg': 'Formulário inválido.'}
            return render(request, 'mudar_senha.html', context)

class SupervisorCrud(Crud):
    model = Supervisor
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['nome', 'celular', 'setor']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        form_class = SupervisorForm
        group_required = ['Supervisor']

    class UpdateView(crud.base.CrudUpdateView):
        form_class = SupervisorEditForm

        @property
        def layout_key(self):
            return 'SupervisorEdit'

    class DetailView(crud.base.CrudDetailView):

        @property
        def layout_key(self):
            return 'SupervisorEdit'

    class DeleteView(crud.base.CrudDeleteView):
        def delete(self, request, *args, **kwargs):
            context =  super(crud.base.CrudDeleteView, self).delete(
                request, args, kwargs)
            self.object.user.delete()
            return redirect(self.get_success_url())

class AlunoCrud(Crud):
    model = Aluno
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['nome', 'celular', 'disciplina']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        form_class = AlunoForm
        group_required = ['Supervisor']


    class UpdateView(crud.base.CrudUpdateView):
        form_class = AlunoEditForm

        @property
        def layout_key(self):
            return 'AlunoEdit'

    class DetailView(crud.base.CrudDetailView):

        @property
        def layout_key(self):
            return 'AlunoEdit'

    class DeleteView(crud.base.CrudDeleteView):

        def delete(self, request, *args, **kwargs):
            self.object.user.delete()
            return redirect(self.get_success_url())


class RecepcionistaCrud(Crud):
    model = Recepcionista
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['nome', 'setor']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        form_class = RecepcionistaForm
        group_required = ['Recepcionista', 'Supervisor']

    class UpdateView(crud.base.CrudUpdateView):
        form_class = RecepcionistaEditForm

        @property
        def layout_key(self):
            return 'RecepcionistaEdit'

    class DetailView(crud.base.CrudDetailView):

        @property
        def layout_key(self):
            return 'RecepcionistaEdit'

    class DeleteView(crud.base.CrudDeleteView):
        def delete(self, request, *args, **kwargs):
            context =  super(crud.base.CrudDeleteView, self).delete(
                request, args, kwargs)
            self.object.user.delete()
            return redirect(self.get_success_url())


class FisioterapiaAvaliacaoGestacionalCrud(Crud):
    model = FisioterapiaAvaliacaoGestacional
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Fisioterapêutica Gestacional'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaAvaliacaoGestacional.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaavaliacaogestacional_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaAvaliacaoMasculinaCrud(Crud):
    model = FisioterapiaAvaliacaoMasculina
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação de Incontinência Urinária Masculina'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaAvaliacaoMasculina.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaavaliacaomasculina_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaAvaliacaoFemininaCrud(Crud):
    model = FisioterapiaAvaliacaoFeminina
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação de Incontinência Urinária Feminina'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaAvaliacaoFeminina.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaavaliacaofeminina_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()

class FisioterapiaAcidenteVascularEncefalicoCrud(Crud):
    model = FisioterapiaAcidenteVascularEncefalico
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Acidente Vascular Encefálico'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaAcidenteVascularEncefalico.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaacidentevascularencefalico_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaEscleroseMultiplaCrud(Crud):
    model = FisioterapiaEscleroseMultipla
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Esclerose Múltipla'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaEscleroseMultipla.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaesclerosemultipla_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaTRMCrud(Crud):
    model = FisioterapiaTRM
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação TRM'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaTRM.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiatrm_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()




class FisioterapiaNeurologicaCrud(Crud):
    model = FisioterapiaNeurologica
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Neurológica'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaNeurologica.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapianeurologica_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaParkinsonCrud(Crud):
    model = FisioterapiaParkinson
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data', 'exame_total']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Parkinson'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaParkinson.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):
        form_class = FisioterapiaParkinsonForm

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaparkinson_list',
                        kwargs={'pk': self.kwargs['pk']})


        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()

    class UpdateView(crud.base.CrudUpdateView):
        form_class = FisioterapiaParkinsonForm


class FisioterapiaParalisiaFacialCrud(Crud):
    model = FisioterapiaParalisiaFacial
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Avaliação Paralisia Facil'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaParalisiaFacial.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):
        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaparalisiafacial_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data_nascimento'] = paciente.data_nascimento
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaOrtopediaReavaliacaoCrud(Crud):
    model = FisioterapiaOrtopediaReavaliacao
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Ficha de Reavaliação'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaOrtopediaReavaliacao.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):
        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaortopediareavaliacao_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            return self.initial.copy()


class FisioterapiaOrtopediaAvaliacaoCrud(Crud):
    model = FisioterapiaOrtopediaAvaliacao
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['data']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class ListView(crud.base.CrudListView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/list$'

        def get_context_data(self, **kwargs):
            context = super(crud.base.CrudListView, self).get_context_data(
                **kwargs)
            context['NO_ENTRIES_MSG'] = 'Nenhuma ficha encontrada.'
            context['pk'] = self.kwargs['pk']
            context['title'] = 'Ficha de Avaliação'
            context['headers'] = self.get_headers()
            context['rows'] = self.get_rows(
                    FisioterapiaOrtopediaAvaliacao.objects.filter(
                        paciente_id=self.kwargs['pk']))
            return context

    class CreateView(crud.base.CrudCreateView):
        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/create$'

        def cancel_url(self):
            return reverse('usuarios:fisioterapiaortopediaavaliacao_list',
                        kwargs={'pk': self.kwargs['pk']})

        def get_initial(self):
            paciente = Paciente.objects.get(id=self.kwargs['pk'])
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['data'] = datetime.now().strftime('%d/%m/%Y')
            self.initial['data_nascimento'] = paciente.data_nascimento
            return self.initial.copy()
