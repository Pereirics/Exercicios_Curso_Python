from random import randint
from pygame import time
print('=-' * 20)
print('PAR OU ÍMPAR')
print('=-' * 20)
cont = 1

while True:
    n1 = int(input('Escreva um número: '))
    n2 = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print('-' * 30)
    pc = randint(1,9)
    s = n1 + pc
    if s % 2 == 0:
        ai = 'PAR'
    else:
        ai = 'ÍMPAR'
    print('O computador está a escolher...')
    time.delay(1000)
    print('-' * 30)
    print(f'Tu jogaste {n1} e o computador {pc}. Total de {n1 + pc} DEU {ai}')
    print('-' * 30)
    time.delay(1000)
    if s % 2 == 0 and n2 == 'P':
        print('Você VENCEU!')
        print('Vamos jogar de novo...')
        cont += 1
    elif s % 2 != 0 and n2 == 'I':
        print('Você VENCEU!')
        print('Vamos jogar de novo...')
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break
print(f'GAME OVER! Você venceu {cont} vezes!')



