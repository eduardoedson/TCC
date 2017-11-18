from django.conf.urls import include, url

from .views import (AlunoCrud, SupervisorCrud, FisioterapiaBergCrud,
                    FisioterapiaEvolucaoCrud,
                    FisioterapiaGeriatriaAnamneseCrud,
                    FisioterapiaGeriatriaAvalicaoCrud,
                    FisioterapiaNeurologiaInfantilAvalicaoCrud,
                    FisioterapiaTriagemCrud, PacienteCrud, administradores,
                    mudar_senha, RecepcionistaCrud,
                    FisioterapiaAvaliacaoGestacionalCrud,
                    FisioterapiaAvaliacaoMaculinaCrud)

app_name = 'usuarios'

urlpatterns = [
    url(r'^supervisor/', include(SupervisorCrud.get_urls())),
    url(r'^aluno/', include(AlunoCrud.get_urls())),
    url(r'^recepcionista/', include(RecepcionistaCrud.get_urls())),
    url(r'^paciente/', include(PacienteCrud.get_urls())),
    url(r'^fisioterapia-triagem/', include(FisioterapiaTriagemCrud.get_urls())),
    url(r'^fisioterapia-evolucao/', include(FisioterapiaEvolucaoCrud.get_urls())),
    url(r'^fisioterapia-geriatria-avaliacao/', include(FisioterapiaGeriatriaAvalicaoCrud.get_urls())),
    url(r'^fisioterapia-geriatria-berg/', include(FisioterapiaBergCrud.get_urls())),
    url(r'^fisioterapia-geriatria-anamnese/', include(FisioterapiaGeriatriaAnamneseCrud.get_urls())),
    url(r'^fisioterapia-uroginecologia-avaliacao/', include(FisioterapiaAvaliacaoGestacionalCrud.get_urls())),
    url(r'^fisioterapia-uroginecologia-masculina/', include(FisioterapiaAvaliacaoMaculinaCrud.get_urls())),
    url(r'^fisioterapia-neurologia-infantil-avaliacao/', include(FisioterapiaNeurologiaInfantilAvalicaoCrud.get_urls())),
    url(r'^mudar_senha/$', mudar_senha, name='mudar_senha'),
    url(r'^administradores/$', administradores, name='administradores'),
]
