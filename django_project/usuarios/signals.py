from blessings import Terminal


def criar_setor_biomedicina(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Biomedicina',
        nome='Clínica Escola de Biomedicina')

    t = Terminal()
    print (t.red('\nSetor \'Biomedicina\' criado!'))


def criar_setor_educacao_fisica(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Educação Física',
        nome='Clínica Escola de Educação Física')

    t = Terminal()
    print (t.red('\nSetor \'Educação Física\' criado!'))


def criar_setor_enfermagem(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Enfermagem',
        nome='Clínica Escola de Enfermagem')

    t = Terminal()
    print (t.red('\nSetor \'Enfermagem\' criado!'))


def criar_setor_farmacia(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Farmácia',
        nome='Clínica Escola de Farmácia')

    t = Terminal()
    print (t.red('\nSetor \'Farmácia\' criado!'))


def criar_setor_fisioterapia(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Fisioterapia',
        nome='Clínica Escola de Fisioterapia')

    t = Terminal()
    print (t.red('\nSetor \'Fisioterapia\' criado!'))


def criar_setor_medicina(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Medicina',
        nome='Clínica Escola de Medicina')

    t = Terminal()
    print (t.red('\nSetor \'Medicina\' criado!'))


def criar_setor_nutricao(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Nutrição',
        nome='Clínica Escola de Nutrição')

    t = Terminal()
    print (t.red('\nSetor \'Nutrição\' criado!'))


def criar_setor_odontologia(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Odontologia',
        nome='Clínica Escola de Odontologia')

    t = Terminal()
    print (t.red('\nSetor \'Odontologia\' criado!'))


def criar_setor_psicologia(sender, **kwargs):
    from servicos.models import Setor

    Setor.objects.get_or_create(
        descricao='Psicologia',
        nome='Clínica Escola de Psicologia')

    t = Terminal()
    print (t.red('\nSetor \'Psicologia\' criado!'))


def criar_disciplinas_biomedicina(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Saúde Coletiva I',
        'Saúde Coletiva II',
        'Saúde Coletiva III',
    ]
    setor = Setor.objects.get(descricao='Biomedicina')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Biomedicina foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Biomedicina'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_educacao_fisica(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Estágio Supervisonado I',
        'Estágio Supervisonado II',
        'Estágio Supervisonado III',
    ]
    setor = Setor.objects.get(descricao='Educação Física')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Educação Física foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Educação Física'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_enfermagem(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Estágio Supervisonado I',
        'Estágio Supervisonado II',
        'Estágio Supervisonado III',
    ]
    setor = Setor.objects.get(descricao='Enfermagem')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Enfermagem foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Enfermagem'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_farmacia(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Estágio Supervisonado I',
        'Estágio Supervisonado II',
        'Estágio Supervisonado III',
    ]
    setor = Setor.objects.get(descricao='Farmácia')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Farmácia foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Farmácia'):
        print (t.blue('  - ' + disciplina.descricao))


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
    for disciplina in Disciplina.objects.filter(setor__descricao='Fisioterapia'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_medicina(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Prática em Clínica Cirurgica I',
        'Prática em Clínica Cirurgica II',
        'Prática em Clínica Cirurgica III',
    ]
    setor = Setor.objects.get(descricao='Medicina')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Medicina foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Medicina'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_nutricao(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Estágio Supervisonado I',
        'Estágio Supervisonado II',
        'Estágio Supervisonado III',
    ]
    setor = Setor.objects.get(descricao='Nutrição')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Nutrição foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Nutrição'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_odontologia(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Estágio Supervisonado I',
        'Estágio Supervisonado II',
        'Estágio Supervisonado III',
    ]
    setor = Setor.objects.get(descricao='Odontologia')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Odontologia foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Odontologia'):
        print (t.blue('  - ' + disciplina.descricao))


def criar_disciplinas_psicologia(sender, **kwargs):
    from servicos.models import Disciplina, Setor

    disciplinas = [
        'Psicologia Social I',
        'Psicologia Social II',
        'Psicologia Social III',
    ]
    setor = Setor.objects.get(descricao='Psicologia')

    for disciplina in disciplinas:
        Disciplina.objects.get_or_create(setor=setor, descricao=disciplina)

    t = Terminal()
    print (t.blue('\nAs seguintes disciplinas de Psicologia foram criadas:'))
    for disciplina in Disciplina.objects.filter(setor__descricao='Psicologia'):
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
