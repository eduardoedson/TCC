from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_migrate
from usuarios.signals import *


class UsuariosConfig(AppConfig):
    name = 'usuarios'
    verbose_name = _('Usuários Config')

    def ready(self):
        post_migrate.connect(criar_setor_biomedicina, sender=self)
        post_migrate.connect(criar_setor_educacao_fisica, sender=self)
        post_migrate.connect(criar_setor_enfermagem, sender=self)
        post_migrate.connect(criar_setor_farmacia, sender=self)
        post_migrate.connect(criar_setor_fisioterapia, sender=self)
        post_migrate.connect(criar_setor_medicina, sender=self)
        post_migrate.connect(criar_setor_nutricao, sender=self)
        post_migrate.connect(criar_setor_odontologia, sender=self)
        post_migrate.connect(criar_setor_psicologia, sender=self)
        post_migrate.connect(criar_disciplinas_biomedicina, sender=self)
        post_migrate.connect(criar_disciplinas_educacao_fisica, sender=self)
        post_migrate.connect(criar_disciplinas_enfermagem, sender=self)
        post_migrate.connect(criar_disciplinas_farmacia, sender=self)
        post_migrate.connect(criar_disciplinas_fisioterapia, sender=self)
        post_migrate.connect(criar_disciplinas_medicina, sender=self)
        post_migrate.connect(criar_disciplinas_nutricao, sender=self)
        post_migrate.connect(criar_disciplinas_odontologia, sender=self)
        post_migrate.connect(criar_disciplinas_psicologia, sender=self)
        post_migrate.connect(criar_superuser, sender=self)
        post_migrate.connect(criar_supervisor_fisioterapia, sender=self)
        post_migrate.connect(criar_recepcionista_fisioterapia, sender=self)
