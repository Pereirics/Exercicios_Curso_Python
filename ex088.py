from random import randint
from pygame import time
print('-' * 30)
print(' ' * 5, 'JOGA NO EUROMILHÕES')
print('-' * 30)
vezes = int(input('Quantas chaves quer que eu gere? '))
print(f'-=-== A SORTEAR {vezes} JOGOS -=-=-=')
for c in range(0, vezes):
    lista = [[], []]
    print(f'Jogo {c + 1:^3}: ', end='')
    a = randint(1, 50)
    for d in range(0, 5):
        if a not in lista[0]:
            d -= 1
        lista[0].append(a)
        a = randint(1, 50)
    b = randint(1, 10)
    for e in range(0, 2):
        if b in lista[1]:
            e -= 1
        lista[1].append(b)
        b = randint(1, 10)
    lista[0].sort()
    lista[1].sort()
    print(lista[0],lista[1])
    lista.clear()
    time.delay(800)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)

