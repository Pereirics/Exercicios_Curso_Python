tup = int(input('Escreva um número: ')), int(input('Escreva um número: ')), int(input('Escreva um número: ')), int(input('Escreva um número: '))
print(f'O 9 apareceu {tup.count(9)} vezes')
print(f'O 3 apareceu pela primeira vez {tup.index(3) + 1}ª posição')
print('Os números pares inseridos foram: ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')
