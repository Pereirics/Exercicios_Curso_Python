import pygame

n1 = float(input('Escreva um número: '))
print('A processar...')
pygame.time.delay(1000)
print(f'A tabuada do número {n1} é: ')
pygame.time.delay(500)

for c in range(1,11):
    print(f'{n1} x {c} = {n1 * c :.2f}')
    pygame.time.delay(150)