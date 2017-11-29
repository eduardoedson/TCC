from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_migrate
from blessings import Terminal

def criar_superuser(sender, **kwargs):
    from django.contrib.auth.models import User

    username = 'prontuario_ucb'
    username = 'prontuario_2017'

    User.objects.filter(username='prontuario_ucb').exists() or \
    User.objects.create_superuser('prontuario_ucb', 'prontuario@ucb.br', 'prontuario_2017')

    t = Terminal()
    print (t.yellow('\n\n\nSuperusuário criado!\nLogin: prontuario_ucb\nSenha: prontuario_2017\n\n\n'))

class UsuariosConfig(AppConfig):
    name = 'usuarios'
    verbose_name = _('Usuários Config')

    def ready(self):
        post_migrate.connect(criar_superuser, sender=self)
