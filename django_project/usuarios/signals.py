from blessings import Terminal


def criar_setor_fisioterapia(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Fisioterapia',
        nome='Clínica Escola de Fisioterapia')

    t = Terminal()
    print (t.red('\nSetor \'Fisioterapia\' criado!'))


def criar_areas_fisioterapia(sender, **kwargs):
    from servicos.models import AreaAtendimento, Setor

    areas = [
        'Geriatria',
        'Neurologia Adulto',
        'Neurologia Infantil',
        'Ortopedia',
        'Uroginecologia',
    ]
    setor = Setor.objects.get(descricao='Fisioterapia')

    for area in areas:
        AreaAtendimento.objects.get_or_create(setor=setor, descricao=area)

    t = Terminal()
    print (t.green('\nAs seguintes áreas de atendimento de Fisioterapia foram criadas:'))
    for area in AreaAtendimento.objects.all():
        print (t.green('  - ' + area.descricao))


def criar_disciplinas_fisioterapia(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Estágio Geriatria',
        'Estágio Neurologia Adulto',
        'Estágio Neurologia Infantil',
        'Estágio Ortopedia',
        'Estágio Uroginecologia',
    ]
    setor = Setor.objects.get(descricao='Fisioterapia')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Fisioterapia foram criadas:'))
    for disciplina in Disciplina.objects.all():
        print (t.blue('  - ' + disciplina.descricao))


def criar_superuser(sender, **kwargs):
    from django.contrib.auth.models import User

    username = 'prontuario_ucb'
    password = 'prontuario_2017'

    User.objects.filter(username=username).exists() or \
    User.objects.create_superuser(username, 'prontuario@ucb.br', password)

    t = Terminal()
    print (t.yellow('\nSuperusuário criado!\n  - Login: ' + username + '\n  - Senha: ' + password))


def criar_supervisor_fisioterapia(sender, **kwargs):
    from servicos.models import Setor
    from usuarios.models import Supervisor
    from django.contrib.auth.models import User
    from utils import get_or_create_grupo

    setor = Setor.objects.get(descricao='Fisioterapia')

    username = 'supervisor_fisioterapia'
    password = 'prontuario_2017'

    u = User.objects.get_or_create(username=username)
    u[0].set_password(password)
    u[0].is_active = True
    u[0].groups.add(get_or_create_grupo('Supervisor'))
    u[0].save()

    Supervisor.objects.get_or_create(
        nome='Supervisor Fisioterapia',
        sexo='O',
        setor=setor,
        user=u[0],
        username=username
    )

    t = Terminal()
    print (t.magenta('\nSupervisor de Fisioterapia criado!\n  - Login: ' + username + '\n  - Senha: ' + password))


def criar_recepcionista_fisioterapia(sender, **kwargs):
    from servicos.models import Setor
    from usuarios.models import Recepcionista
    from django.contrib.auth.models import User
    from utils import get_or_create_grupo

    setor = Setor.objects.get(descricao='Fisioterapia')

    username = 'recepcao_fisioterapia'
    password = 'prontuario_2017'

    u = User.objects.get_or_create(username=username)
    u[0].set_password(password)
    u[0].is_active = True
    u[0].groups.add(get_or_create_grupo('Recepcionista'))
    u[0].save()

    Recepcionista.objects.get_or_create(
        nome='Recepção Fisioterapia',
        sexo='O',
        setor=setor,
        user=u[0],
        username=username
    )

    t = Terminal()
    print (t.cyan('\nRecepção de Fisioterapia criado!\n  - Login: ' + username + '\n  - Senha: ' + password))
