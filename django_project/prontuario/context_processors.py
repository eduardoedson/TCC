from django.core.exceptions import ObjectDoesNotExist

from usuarios.models import Atendente, Coordenador


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
                coordenador = Coordenador.objects.get(user_id=user.pk)
            except ObjectDoesNotExist:
                try:
                    atendente = Atendente.objects.get(user_id=user.pk)
                except ObjectDoesNotExist:
                    return [0, None]
                else:
                    return [atendente.pk, 'Atendente']
            else:
                return [coordenador.pk, 'Coordenador']
        else:
            return [-1, None]


def recupera_usuario(user_pk, tipo):
    if tipo == 'adm':
        context = {'user_pk': user_pk,
                   'nome': 'Admin',
                   'tipo': 'Administrador'}
    elif user_pk == -1:
        context = {'user_pk': user_pk,
                   'nome': 'Desconhecido',
                   'tipo': 'Desconhecido'}
    else:
        if tipo == 'Coordenador':
            coordenador = Coordenador.objects.get(pk=user_pk)
            context = {'user_pk': user_pk,
                       'nome': coordenador.nome,
                       'setor': coordenador.setor.descricao,
                       'tipo': 'Coordenador',
                       'adm': coordenador.user.is_superuser}
        elif tipo == 'Atendente':
            atendente = Atendente.objects.get(pk=user_pk)
            context = {'user_pk': user_pk,
                       'nome': atendente.nome,
                       'disciplina': atendente.disciplina.descricao,
                       'tipo': 'Atendente',
                       'adm': False}
        else:
            context = {'user_pk': user_pk,
                       'nome': 'Desconhecido',
                       'tipo': 'Desconhecido'}
    return context


def usuario_context(request):
    ret = recupera_user(request)
    return recupera_usuario(ret[0], ret[1])
