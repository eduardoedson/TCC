from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_migrate
from usuarios.signals import (criar_superuser, criar_setor_fisioterapia,
                              criar_areas_fisioterapia,
                              criar_disciplinas_fisioterapia,
                              criar_supervisor_fisioterapia,
                              criar_recepcionista_fisioterapia)


class UsuariosConfig(AppConfig):
    name = 'usuarios'
    verbose_name = _('Usuários Config')

    def ready(self):
        post_migrate.connect(criar_setor_fisioterapia, sender=self)
        post_migrate.connect(criar_areas_fisioterapia, sender=self)
        post_migrate.connect(criar_disciplinas_fisioterapia, sender=self)
        post_migrate.connect(criar_superuser, sender=self)
        post_migrate.connect(criar_supervisor_fisioterapia, sender=self)
        post_migrate.connect(criar_recepcionista_fisioterapia, sender=self)
