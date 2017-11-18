from django.core.exceptions import ObjectDoesNotExist

from usuarios.models import Aluno, Supervisor


def recupera_user(request):
    try:
        user = request.user
    except:
        return [0, None]
    else:
        if user:
            if user.is_superuser:
                return [user.pk, 'adm']
            try:
                supervisor = Supervisor.objects.get(user_id=user.pk)
            except ObjectDoesNotExist:
                try:
                    aluno = Aluno.objects.get(user_id=user.pk)
                except ObjectDoesNotExist:
                    return [0, None]
                else:
                    return [aluno.pk, 'Aluno']
            else:
                return [supervisor.pk, 'Supervisor']
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
                       'adm': supervisor.user.is_superuser}
        elif tipo == 'Aluno':
            aluno = Aluno.objects.get(pk=user_pk)
            context = {'user_pk': user_pk,
                       'nome': aluno.nome,
                       'disciplina': aluno.disciplina.descricao,
                       'tipo': 'Aluno',
                       'adm': False}
        else:
            context = {'user_pk': user_pk,
                       'nome': 'Desconhecido',
                       'tipo': 'Desconhecido'}
    return context


def usuario_context(request):
    ret = recupera_user(request)
    return recupera_usuario(ret[0], ret[1])
