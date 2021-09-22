def leiaInt(texto):
    print('-' * 30)
    while True:
        print(texto, end='')
        n1 = input()
        if n1.isnumeric():
            break
        else:
            print('\033[0:31mERRO! Escreva um número inteiro válido.\033[m')
    return n1


n = leiaInt('Escreva um número: ')
print(f'Você acabou de escrever o número: {n}')
