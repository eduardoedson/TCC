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

from .forms import (AtendenteEditForm, AtendenteForm, CoordenadorEditForm,
                    CoordenadorForm, FisioterapiaBergForm, MudarSenhaForm)
from .models import (Atendente, Coordenador, FisioterapiaBerg,
                     FisioterapiaEvolucao, FisioterapiaGeriatriaAnamnese,
                     FisioterapiaGeriatriaAvalicao,
                     FisioterapiaNeurologiaInfantilAvalicao,
                     FisioterapiaTriagem, Paciente)


def get_medico(pk):
    try:
        coordenador = Coordenador.objects.get(user_id=pk)
    except ObjectDoesNotExist:
        try:
            atendente = Atendente.objects.get(user_id=pk)
        except ObjectDoesNotExist:
            return 0
        else:
            return [atendente, atendente.disciplina.setor.descricao]
    else:
        return [coordenador, coordenador.setor.descricao]


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

            self.initial[
                'data_nascimento'] = paciente.data_nascimento.strftime(
                    '%d/%m/%Y')
            self.initial['sexo'] = paciente.sexo
            self.initial['paciente'] = self.kwargs['pk']
            self.initial['diagnostico_clinico'] = triagem.diagnostico

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
            self.initial['diagnostico'] = triagem.diagnostico
            self.initial['queixa_principal'] = triagem.queixa_principal

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
            medico, especialidade = get_medico(self.request.user.id)
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
            medico, especialidade = get_medico(self.request.user.id)
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

class CoordenadorCrud(Crud):
    model = Coordenador
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['nome', 'celular', 'setor']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        form_class = CoordenadorForm
        group_required = ['Coordenador']

    class UpdateView(crud.base.CrudUpdateView):
        form_class = CoordenadorEditForm

        @property
        def layout_key(self):
            return 'CoordenadorEdit'

    class DetailView(crud.base.CrudDetailView):

        @property
        def layout_key(self):
            return 'CoordenadorEdit'

    class DeleteView(crud.base.CrudDeleteView):
        def delete(self, request, *args, **kwargs):
            context =  super(crud.base.CrudDeleteView, self).delete(
                request, args, kwargs)
            self.object.user.delete()
            return redirect(self.get_success_url())

class AtendenteCrud(Crud):
    model = Atendente
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['nome', 'celular', 'disciplina']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        form_class = AtendenteForm
        group_required = ['Coordenador']


    class UpdateView(crud.base.CrudUpdateView):
        form_class = AtendenteEditForm

        @property
        def layout_key(self):
            return 'AtendenteEdit'

    class DetailView(crud.base.CrudDetailView):

        @property
        def layout_key(self):
            return 'AtendenteEdit'

    class DeleteView(crud.base.CrudDeleteView):
        
        def delete(self, request, *args, **kwargs):
            self.object.user.delete()
            return redirect(self.get_success_url())


def administradores(request):

    if (not request.user.is_authenticated() or
            request.user.groups.first().name != 'Coordenador'):
        return render(request, '403.html', {})

    if request.method == 'GET':
        coords = Coordenador.objects.all()
        adms = []
        for c in coords:
            adm = {'id': c.id,
                   'nome': c.nome,
                   'is_staff': c.user.is_superuser}
            adms.append(adm)

        context = {'adm_list': adms}
        return render(request, 'administradores.html', context)

    elif request.method == 'POST':
        for id_coordenador in request.POST:
            if id_coordenador != 'csrfmiddlewaretoken':
                try:
                    coordenador = Coordenador.objects.get(id=id_coordenador)
                except ObjectDoesNotExist:
                    pass
                else:
                    user = coordenador.user
                    user.is_superuser = request.POST[id_coordenador]
                    user.save()
        return render(request,
                      'index.html',
                      {'msg':
                       'Lista de administradores atualizada com sucesso.'})
