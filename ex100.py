from random import randint
from pygame import time


def sorteia(lista):
    print('Sorteando 5 valores da lista: ')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        time.wait(200)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = []
sorteia(num)
somaPar(num)
