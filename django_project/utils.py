from datetime import date

from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

RANGE_MESES = [
    (1, _('Janeiro')),
    (2, _('Fevereiro')),
    (3, _('Março')),
    (4, _('Abril')),
    (5, _('Maio')),
    (6, _('Junho')),
    (7, _('Julho')),
    (8, _('Agosto')),
    (9, _('Setembro')),
    (10, _('Outubro')),
    (11, _('Novembro')),
    (12, _('Dezembro')),
]

RANGE_ANOS = [(year, year) for year in range(date.today().year, 1889, -1)]

RANGE_SEXO = [('F', _('Feminino')), ('M', _('Masculino')), ('O', _('Outro'))]

YES_NO_CHOICES = [(None, _('----')), ('Não', _('Não')), ('Sim', _('Sim'))]

def from_to(start, end):
    return list(range(start, end + 1))


def make_pagination(index, num_pages):
    PAGINATION_LENGTH = 10
    if num_pages <= PAGINATION_LENGTH:
        return from_to(1, num_pages)
    else:
        if index - 1 <= 5:
            tail = [num_pages - 1, num_pages]
            head = from_to(1, PAGINATION_LENGTH - 3)
        else:
            if index + 1 >= num_pages - 3:
                tail = from_to(index - 1, num_pages)
            else:
                tail = [index - 1, index, index + 1,
                        None, num_pages - 1, num_pages]
            head = from_to(1, PAGINATION_LENGTH - len(tail) - 1)
        return head + [None] + tail

def valida_igualdade(texto1, texto2):
    if texto1 != texto2:
        return False
    return True

def get_or_create_grupo(nome):
    g = Group.objects.get_or_create(name=nome)
    return g[0]

def lista_grupos():
    grupos = []
    for g in Group.objects.all():
        grupos.append(g.name)
    return grupos


ESCALA_FUNCIONAL_BERG = [
    [],
    [
        (4, _('[4] - Capaz de levantar-se sem utilizar as mãos e estabilizar-se independentemente.')),
        (3, _('[3] - Capaz de levantar-se independentemente utilizando as mãos.')),
        (2, _('[2] - Capaz de levantar-se utilizando as mãos após diversas tentativas.')),
        (1, _('[1] - Necessita de ajuda mínima para levantar-se ou estabilizar-se.')),
        (0, _('[0] - Necessita de ajuda moderada ou máxima para levantar-se.')),
    ],
    [
        (4, _('[4] - Capaz de permanecer em pé com segurança por 2 minutos.')),
        (3, _('[3] - Capaz de permanecer em pé por 2 minutos com supervisão.')),
        (2, _('[2] - Capaz de permanecer em pé por 30 segundos sem apoio.')),
        (1, _('[1] - Necessita de várias tentativas para permanecer em pé por 30 segundos sem apoio.')),
        (0, _('[0] - Incapaz de permanecer em pé por 30 segundos sem apoio.')),
    ],
    [
        (4, _('[4] - Capaz de permanecer sentado com segurança e com firmeza por 2 minutos.')),
        (3, _('[3] - Capaz de permanecer sentado por 2 minutos sob supervisão.')),
        (2, _('[2] - Capaz de oermanecer sentado por 30 segundos.')),
        (1, _('[1] - Capaz de permanecer sentado por 10 segundos.')),
        (0, _('[0] - Incapaz de permanecer sentado sem apoio durante 10 segundos.')),
    ],
    [
        (4, _('[4] - Senta-se com segurança com uso mínimo das mãos')),
        (3, _('[3] - Controla a descida utilizando as mãos.')),
        (2, _('[2] - Utiliza a parte posterior das pernas contra a cadeira para controlar a descida.')),
        (1, _('[1] - Senta-se independentemente, mas tem descida sem controle.')),
        (0, _('[0] - Necessita de ajuda para sentar-se.')),
    ],
    [
        (4, _('[4] - Capaz de transferir-se com segurança com uso mínimo das mãos.')),
        (3, _('[3] - Caoaz de transferir-se com segurança com o uso das mãos.')),
        (2, _('[2] - Capaz de transferir-se seguindo orentações verbais e/ou supervisão.')),
        (1, _('[1] - Necessita de uma pessoa para ajudar.')),
        (0, _('[0] - Necessita de duas pessoas para ajudar ou supervisionar para realizar a tarefa com segurança.')),
    ],
    [
        (4, _('[4] - Capaz de permanecer em pé por 10 segundos com segurança.')),
        (3, _('[3] - Capaz de permanecer em pé por 10 segundos com supervisão.')),
        (2, _('[2] - Capaz de permanecer em pé por 3 segundos.')),
        (1, _('[1] - Incapaz de permanecer com os olhos fechados durante 3 segundos, mas mantém-se em pé.')),
        (0, _('[0] - Necessita de ajuda para não cair.')),
    ],
    [
        (4, _('[4] - Capaz de posicionar os pés juntos independentemente e permanecer por 1 minuto com segurança.')),
        (3, _('[3] - Capaz de posicionar os pés juntos independentemente e permanecer por 1 minuto com supervisão.')),
        (2, _('[2] - Capaz de posicionar os pés juntos independentemente e permanecer por 30 segundos.')),
        (1, _('[1] - Necessita de ajuda para posicionar-se, mas é capaz de peranecer com os pés juntos durante 15 segundos.')),
        (0, _('[0] - Necessita de ajuda para posicionar-se e é incapaz de permanecer nessa posição por 15 segundos.')),
    ],
    [
        (4, _('[4] - Pode avançar à frente mais que 25 cm com segurança.')),
        (3, _('[3] - Pode avançar à frente mais que 12,5 cm com segurança.')),
        (2, _('[2] - Pode avançar à frente mais que 5 cm com segurança.')),
        (1, _('[1] - Pode avançar à frente, mas necessita de supervisão.')),
        (0, _('[0] - Perde o equilíbrio na tentativa, ou necessita de apoio externo.')),
    ],
    [
        (4, _('[4] - Capaz de pegar o chinelo com facilidade e segurança.')),
        (3, _('[3] - Capaz de pegar o chinelo, mas necessita de supervisão.')),
        (2, _('[2] - Incapaz de pegá-lo, mas se estica até ficar a 2-5 cm do chinelo e mantém o equilíbrio independentemente.')),
        (1, _('[1] - Incapaz de pegá-lo, necessitando de supervisão enquanto está tentando.')),
        (0, _('[0] - Incapaz de tentar, ou necessita de ajuda para não perder o equilíbrio ou cair.')),
    ],
    [
        (4, _('[4] - Olha para trás de ambos os lados com uma boa distribuição do peso.')),
        (3, _('[3] - Olha para trás somente de um lado, o lado contrário demonstra menor distribuição do peso.')),
        (2, _('[2] - Vira somente para os lados, mas mantém o quilíbrio.')),
        (1, _('[1] - Necessita de supervisão para virar.')),
        (0, _('[0] - Necessita de ajuda para não perder o equilíbrio ou cair.')),
    ],
    [
        (4, _('[4] - Capaz de girar 360 graus com segurança em 4 segundos ou menos.')),
        (3, _('[3] - Capaz de girar 360 graus com segurança somente para um lado em 4 segundos ou menos.')),
        (2, _('[2] - Capaz de girar 360 graus com segurança, mas lentamente.')),
        (1, _('[1] - Necessita de supervisão próxima ou orientações verbais.')),
        (0, _('[0] - Necessita de ajuda enquanto gira.')),
    ],
    [
        (4, _('[4] - Capaz de permanecer em pé independentemente e com segurança, completando 8 movimentos em 20 segundos.')),
        (3, _('[3] - Capaz de permanecer em pé independentemente e completar 8 movimentos em mais que 20 segundos.')),
        (2, _('[2] - Capaz de completar 4 movimentos sem ajuda.')),
        (1, _('[1] - Capaz de completar mais que 2 movimentos com o mínimo de ajuda.')),
        (0, _('[0] - Incapaz de tentar, ou necessita de ajuda para não cair.')),
    ],
    [
        (4, _('[4] - Capaz de colocar um pé imediatamente à frente do outro, independentemente, e permanecer por 30 segundos.')),
        (3, _('[3] - Capaz de colocar um pé um pouco à frente do outro e levemente para o lado, independentemente, e permanecer por 30 segundos.')),
        (2, _('[2] - Capaz de dar um pequeno passo independentemente, e permanecer por 30 segundos.')),
        (1, _('[1] - Necessita de ajuda para dar o passo, porém permanece por 15 segundos.')),
        (0, _('[0] - Perde o equilíbrio ao tentar dar um passo ou ficar de pé.')),
    ],
    [
        (4, _('[4] - Capaz de levantar uma perna independentemente e permanecer por mais que 10 segundos.')),
        (3, _('[3] - Capaz de levantar uma perna independentemente e permanecer por 5-10 segundos.')),
        (2, _('[2] - Capaz de levantar uma perna independentemente e permanecer por mais que 3 segundos.')),
        (1, _('[1] - Tenta levantar uma perna, mas é incapaz de permanecer por 3 segundos, embora permaneça em pé independentemente.')),
        (0, _('[0] - Incapaz de tentar, ou necessita de ajuda para não cair.')),
    ],
]
