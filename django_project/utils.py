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

CONTRACAO = [('[0] - Zero', _('[0] - Zero')), ('[1] - Regular', _('[1] - Regular')), ('[2] - Normal', _('[2] - Normal'))]
TONUS = [('[0] - Atonia', _('[0] - Atonia')), ('[1] - Diminuído ou Aumentado', _('[1] - Diminuído ou Aumentado')), ('[2] - Normal', _('[2] - Normal'))]
SINSINESIAS = [('[0] - Ausência', _('[0] - Ausência')), ('[1] - Inibição Voluntária', _('[1] - Inibição Voluntária')), ('[2] - Inibição Por Pressão Digital', _('[2] - Inibição Por Pressão Digital'))]

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


AVALIACAO_PARKINSON = [
    [],
    [
        (0, _('[0] - Sem comprometimento')),
        (1, _('[1] - Lentificação detectável do uso de supinação - pronação evidenciada pela dificuldade no inicio do manuseio de instrumentos, abotoamento de roupas e durante a escrita manual.')),
        (2, _('[2] - Lentificação moderada de supinação - pronação, em um ou ambos os lados, evidenciada pelo comprometimento moderado da função das mãos. A escrita manual encontra-se fortemente prejudicada, com micrografia presente.')),
        (3, _('[3] - Lentificação grave do uso de supinação - pronação. Incapaz de escrever ou abotoar roupas. Dificuldade acentuada no manuseio de utenspilios.')),
    ],
    [
        (0, _('[0] - Não detectável.')),
        (1, _('[1] - Rigidez detectável no pescoço e ombros. Fenômenos de ativação encontra-se presente. Um ou ambos os braços apresentam rigidez leve, negativa, durante o processo.')),
        (2, _('[2] - Rigidez moderada no pescoço e ombros. A rigidez durante o repouso é positiva quando o paciente não está medicado.')),
        (3, _('[3] - Rigidez grave no pescoço e ombros. A rigidez de repouso não pode ser revertida por medicação.')),
    ],
    [
        (0, _('[0] - Postura normal. Cabeça fletida ara frente menos que 10cm.')),
        (1, _('[1] - Começando a apresentar coluna de atiçador. Cabeça para frente mais de 12cm.')),
        (2, _('[2] - Começa a apresentar flexão de braço. Cabeça fletida para frente mais de 15cm. Um ou ambos os braços elevados mas ainda abaixo da cintura.')),
        (3, _('[3] - Início da postura simiesca. Cabeça fletida para frente mais de 15cm. Uma ou ambas as mãos elevadas acima da cintura. Flexão aguda da mão, começando a flexão de joelhos.')),
    ],
    [
        (0, _('[0] - Balanceio correto dos dois braços.')),
        (1, _('[1] - Um braço com diminuição definida do balanceio.')),
        (2, _('[2] - Um braço não balança.')),
        (3, _('[3] - Os dois braços não balançam.')),
    ],
    [
        (0, _('[0] - Passos bons com passadas de 40 a 75cm. Faz iros sem esforço.')),
        (1, _('[1] - Marcha encurtada para passadas 30 a 40cm. Começando a bater um calcanhar. Faz os giros mais lentamente. Requer vários passos.')),
        (2, _('[2] - Passada moderadamente encurtado agora com 15 a 30cm. Os dois calcanhares começam a bater no solo forçadamente.')),
        (3, _('[3] - Início da marcha com interrupções, passos com menos de 7cm. Ocasionalmente a marcha apresenta um tipo de bloqueio com um "gaguejar". O paciente anda sobre artelhos fazem os giros muito lentamente.')),
    ],
    [
        (0, _('[0] - Sem tremor detectável.')),
        (1, _('[1] - Observando o movimento de tremor com menos de 2,5cm de pico a pico nos membros ou cabeça durante o repouso ou em qualquer mão durante a marcha ou durante o teste dedo-nariz.')),
        (2, _('[2] - O evento máximo do tremor nõ excede 10cm. O tremor é grave mas não constamte paciente retém algum controle das mãos.')),
        (3, _('[3] - Um evento de tremor excedendo 10cm. O tremor é constante e grave. O paciente não consegue livrar-se do tremor enquanto está acordado a menos que seja do tipo cerebelar puro. A escrita e auto-alimentação são impossíveis.')),
    ],
    [
        (0, _('[0] - Normal. Expressão completa. Sem aparência de espanto.')),
        (1, _('[1] - Imobilidade detectável. A boca permanece aberta. Começam características de ansiedade e depressão.')),
        (2, _('[2] - Imobilidade moderada. A emoção é interrompida com aumento acentuado no limiar. Os lábios se partem com o tempo. Aparência moderada de ansiedade ou depressão. Pode ocorrer perda de saliva pela boca.')),
        (3, _('[3] - Face congelada. Boca aberta 0,5cm ou mais. Pode haver perda intensa de saliva pela boca.')),
    ],
    [
        (0, _('[0] - Nenhuma.')),
        (1, _('[1] - Aumento da perspiração, a secreção permanece fina.')),
        (2, _('[2] - Oleosidade óbvia presente. Secreção mais espessa.')),
        (3, _('[3] - Seborréia acentuada toda a face e cabeça cobertas por uma secreção espessa.')),
    ],
    [
        (0, _('[0] - Clara, sonora, ressonante, fácil de entender.')),
        (1, _('[1] - Começando uma rouquidão com perda de inflexão e ressonância. Bom volume e ainda fácil de entender.')),
        (2, _('[2] - Rouquidão e fraqueza moderadas. Monotonia constante, sem variações de altura. Início de disartria, hesitação, gaguejamento; dificuldade para ser compreendida.')),
        (3, _('[3] - Rouquidão e fraqueza acentuadas. Muito difícil para ouvir e compreender.')),
    ],
    [
        (0, _('[0] - Sem comprometimento.')),
        (1, _('[1] - Ainda capaz de todos os cuidados pessoais mas a velocidade com que se veste torna-se um empecílio difinitivo. Capaz de viver sozinho e frequentemente ainda empregado.')),
        (2, _('[2] - Requer ajuda em certas críticas, como para virar-se na cama levantar de cadeiras etc. Muito lento no desempenho da maioria das atividades mas trata esse problema designando mais tempo para cada atividade.')),
        (3, _('[3] - Continuamente incapacitado. Incapaz de vestir-se, alimentar-se ou andar sozinho.')),
    ],
]

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
