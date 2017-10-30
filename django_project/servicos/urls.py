from django.conf.urls import include, url

from .views import DisciplinaCrud, SetorCrud, AreaAtendimentoCrud

app_name = 'servicos'

urlpatterns = [
    url(r'^setor/', include(SetorCrud.get_urls())),
    url(r'^disciplina/', include(DisciplinaCrud.get_urls())),
    url(r'^area-atendimento/', include(AreaAtendimentoCrud.get_urls())),
]
