from django.core.exceptions import ObjectDoesNotExist

from usuarios.models import Aluno, Supervisor, Recepcionista


def recupera_user(request):
    try:
        user = request.user
    except:
        return [0, None]
    else:
        if user.is_superuser:
            return [user.pk, 'adm']
        elif user.groups.first():
            grupo = user.groups.first().name
            if grupo == 'Recepcionista':
                recepcionista = Recepcionista.objects.get(user_id=user.pk)
                return [recepcionista.pk, 'Recepcão']
            elif grupo == 'Aluno':
                aluno = Aluno.objects.get(user_id=user.pk)
                return [aluno.pk, 'Aluno']
            elif grupo == 'Supervisor':
                supervisor = Supervisor.objects.get(user_id=user.pk)
                return [supervisor.pk, 'Supervisor']
            else:
                return [-1, None]
        else:
            return [-1, None]


def recupera_usuario(user_pk, tipo):
    if tipo == 'adm':
        context = {'user_pk': user_pk,
                   'nome': 'Administrador',
                   'tipo': 'Administrador'}
    elif user_pk == -1:
        context = {'user_pk': user_pk,
                   'nome': 'Desconhecido',
                   'tipo': 'Desconhecido'}
    else:
        if tipo == 'Supervisor':
            supervisor = Supervisor.objects.get(pk=user_pk)
            context = {'user_pk': user_pk,
                       'nome': supervisor.nome,
                       'setor': supervisor.setor.descricao,
                       'tipo': 'Supervisor',
                       'adm': False}
        elif tipo == 'Aluno':
            aluno = Aluno.objects.get(pk=user_pk)
            context = {'user_pk': user_pk,
                       'nome': aluno.nome,
                       'disciplina': aluno.disciplina.descricao,
                       'tipo': 'Aluno',
                       'adm': False}
        elif tipo == 'Recepcão':
            recepcionista = Recepcionista.objects.get(pk=user_pk)
            context = {'user_pk': user_pk,
                       'nome': recepcionista.nome,
                       'setor': recepcionista.setor.descricao,
                       'tipo': 'Recepcionista',
                       'adm': False}
        else:
            context = {'user_pk': user_pk,
                       'nome': 'Desconhecido',
                       'tipo': 'Desconhecido'}
    return context


def usuario_context(request):
    ret = recupera_user(request)
    return recupera_usuario(ret[0], ret[1])
