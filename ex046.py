import emoji
import pygame

for c in range(10,-1,-1):
    print(f'{c}!')
    print('...')
    pygame.time.delay(1000)

print(emoji.emojize('FIM! :fireworks:'))
