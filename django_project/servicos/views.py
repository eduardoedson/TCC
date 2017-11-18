from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

import crud.base
from crud.base import Crud
from prontuario.settings import LOGIN_REDIRECT_URL

from .models import AreaAtendimento, Disciplina, Setor


class SetorCrud(Crud):
    model = Setor
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['descricao', 'nome']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        group_required = ['Supervisor']

    class DetailView(crud.base.CrudDetailView):

        def get_context_data(self, **kwargs):
            context = super(DetailView, self).get_context_data(**kwargs)
            context['disciplinas'] = Disciplina.objects.filter(
                setor=self.object)
            return context


class DisciplinaCrud(Crud):
    model = Disciplina
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['descricao', 'setor']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        group_required = ['Supervisor']


class AreaAtendimentoCrud(Crud):
    model = AreaAtendimento
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['setor', 'descricao']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL

    class CreateView(crud.base.CrudCreateView, GroupRequiredMixin):
        group_required = ['Supervisor']
