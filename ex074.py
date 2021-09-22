from random import randint

n1 = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
maior = menor = n1[0]

print('Os números escolhidos foram: ', end='')
for n in n1:
    print(n, end=' ')

print(f'\nO maior sorteado foi o {max(n1)}')
print(f'O menor sorteado foi o {min(n1)}')
