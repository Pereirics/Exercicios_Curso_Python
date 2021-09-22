from pygame import time


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    print(a, end=' ')
    if a < b:
        while a < b:
            a += c
            time.wait(350)
            print(f'{a}', end=' ')
    else:
        while a > b:
            a -= c
            time.wait(350)
            print(f'{a}', end=' ')
    print('FIM!')
    print('-=' * 15)

print('-=' * 15)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua fez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
