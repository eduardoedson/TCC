from django.conf.urls import include, url

from .views import (AtendenteCrud, CoordenadorCrud, PacienteCrud,
                    ProntuarioCrud, administradores, mudar_senha,
                    FisioterapiaTriagemCrud, FisioterapiaEvolucaoCrud,
                    FisioterapiaNeurologiaInfantilAvalicaoCrud,
                    FisioterapiaGeriatriaAvalicaoCrud,
                    FisioterapiaBergCrud)

app_name = 'usuarios'

urlpatterns = [
    url(r'^coordenador/', include(CoordenadorCrud.get_urls())),
    url(r'^atendente/', include(AtendenteCrud.get_urls())),
    url(r'^paciente/', include(PacienteCrud.get_urls())),
    url(r'^prontuario/', include(ProntuarioCrud.get_urls())),
    url(r'^fisioterapia-triagem/', include(FisioterapiaTriagemCrud.get_urls())),
    url(r'^fisioterapia-evolucao/', include(FisioterapiaEvolucaoCrud.get_urls())),
    url(r'^fisioterapia-geriatria-avaliacao/', include(FisioterapiaGeriatriaAvalicaoCrud.get_urls())),
    url(r'^fisioterapia-geriatria-berg/', include(FisioterapiaBergCrud.get_urls())),
    url(r'^fisioterapia-neurologia-infantil-avaliacao/', include(FisioterapiaNeurologiaInfantilAvalicaoCrud.get_urls())),
    url(r'^mudar_senha/$', mudar_senha, name='mudar_senha'),
    url(r'^administradores/$', administradores, name='administradores'),
]
