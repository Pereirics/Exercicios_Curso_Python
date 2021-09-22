from datetime import date


def votar(a):
    """
    -> Função para determinar se uma pessoa pode votar ou não através do seu ano de nascimento
    :param a: ano em que pessoa nasceu
    :return: retorna se pode votar ou não
    """
    atual = date.today().year
    idade = atual - a
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO PERMITIDO'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
resp = votar(ano)
print(resp)
