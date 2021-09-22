from pygame import time


def maior(*num):
    print('-=' * 30)
    print('A analisar os valores passados...')
    cont = maior = 0
    for val in num:
        print(val, end=' ')
        time.wait(300)
        cont += 1
        if cont == 1:
            maior = val
        else:
            if val > maior:
                maior = val
    print(f'Foram passados {cont} valores ao todo.')
    print(f'O maior valor passado foi o {maior}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

