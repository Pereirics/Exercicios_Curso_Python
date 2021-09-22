def fatorial(n, show=0):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta (True ou False)
    :return: O valor fatorial de n
    """
    print('-' * 30)
    mult = n
    n -= 1
    if show:  # o mesmo que show == True, show == False seria if not show
        print(mult, 'x', n, end=' ')
        while n != 1:
            print('x', end=' ')
            mult *= n
            n -= 1
            print(n, end=' ')
        print('=', end=' ')
    else:
        while n != 1:
            mult *= n
            n -= 1
    return mult


print(fatorial(5, True))
help(fatorial)
