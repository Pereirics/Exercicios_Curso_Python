from random import randint
from pygame import time

n = 0
while n != 1:
    p = int(input('Tente adivinhar que número entre 0 e 10 o computador vai escolher: '))
    r = randint(0,10)
    print('A escolher...')
    time.delay(1000)
    if p == r:
        print('Parabéns! Acertou no número!!')
        n = 1
    else:
        print(f'ERROU! Mais sorte na próxima! O computador tinha escolhido o {r}')
        print('------------------------------------------------------------------')