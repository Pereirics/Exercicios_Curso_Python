from random import randint
from pygame import time
from operator import itemgetter
maior = menor = 0
dicio = {}
for c in range(1, 5):
    dicio[f'jogador{c}'] = randint(1, 6)
for k, v in dicio.items():
    print(f'O {k} tirou {v} no dado.')
    time.wait(500)
print('-=' * 30)
print('   == RANKING DOS JOGADORES ==')

ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True) #mete em ordem de valor, se fosse 0 seria pelas keys
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    time.wait(500)