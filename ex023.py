n1 = int(input('Escreva um número entre 0 e 9999: '))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')