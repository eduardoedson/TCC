from django.conf.urls import include, url

from .views import (AlunoCrud, SupervisorCrud, FisioterapiaBergCrud,
                    FisioterapiaEvolucaoCrud,
                    FisioterapiaGeriatriaAnamneseCrud,
                    FisioterapiaGeriatriaAvalicaoCrud,
                    FisioterapiaNeurologiaInfantilAvalicaoCrud,
                    FisioterapiaTriagemCrud, PacienteCrud, administradores,
                    mudar_senha, RecepcionistaCrud,
                    FisioterapiaAvaliacaoGestacionalCrud,
                    FisioterapiaAvaliacaoMasculinaCrud,
                    FisioterapiaAvaliacaoFemininaCrud,
                    FisioterapiaAcidenteVascularEncefalicoCrud,
                    FisioterapiaEscleroseMultiplaCrud,
                    FisioterapiaTRMCrud,
                    FisioterapiaNeurologicaCrud, FisioterapiaParkinsonCrud,
                    FisioterapiaParalisiaFacialCrud)

app_name = 'usuarios'

fisioterapia_urls = [
        url(r'^fisioterapia-triagem/', include(FisioterapiaTriagemCrud.get_urls())),
        url(r'^fisioterapia-evolucao/', include(FisioterapiaEvolucaoCrud.get_urls())),
        url(r'^fisioterapia-geriatria-avaliacao/', include(FisioterapiaGeriatriaAvalicaoCrud.get_urls())),
        url(r'^fisioterapia-geriatria-berg/', include(FisioterapiaBergCrud.get_urls())),
        url(r'^fisioterapia-geriatria-anamnese/', include(FisioterapiaGeriatriaAnamneseCrud.get_urls())),
        url(r'^fisioterapia-uroginecologia-avaliacao/', include(FisioterapiaAvaliacaoGestacionalCrud.get_urls())),
        url(r'^fisioterapia-uroginecologia-masculina/', include(FisioterapiaAvaliacaoMasculinaCrud.get_urls())),
        url(r'^fisioterapia-uroginecologia-feminina/', include(FisioterapiaAvaliacaoFemininaCrud.get_urls())),
        url(r'^fisioterapia-neurologia-infantil-avaliacao/', include(FisioterapiaNeurologiaInfantilAvalicaoCrud.get_urls())),
        url(r'^fisioterapia-neurologia-adulto-avaliacao-ave/', include(FisioterapiaAcidenteVascularEncefalicoCrud.get_urls())),
        url(r'^fisioterapia-neurologia-adulto-esclerose-multipla/', include(FisioterapiaEscleroseMultiplaCrud.get_urls())),
        url(r'^fisioterapia-neurologia-adulto-trm/', include(FisioterapiaTRMCrud.get_urls())),
        url(r'^fisioterapia-neurologia-base/', include(FisioterapiaNeurologicaCrud.get_urls())),
        url(r'^fisioterapia-neurologia-parkinson/', include(FisioterapiaParkinsonCrud.get_urls())),
        url(r'^fisioterapia-neurologia-paralisia-facial/', include(FisioterapiaParalisiaFacialCrud.get_urls())),
]

urlpatterns = [
    url(r'^supervisor/', include(SupervisorCrud.get_urls())),
    url(r'^aluno/', include(AlunoCrud.get_urls())),
    url(r'^recepcionista/', include(RecepcionistaCrud.get_urls())),
    url(r'^paciente/', include(PacienteCrud.get_urls())),
    url(r'^mudar_senha/$', mudar_senha, name='mudar_senha'),
    url(r'^administradores/$', administradores, name='administradores'),
] + fisioterapia_urls
