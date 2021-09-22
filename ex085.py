valores = [[],[]]
for c in range(1,8):
    val = int(input(f'Escreva o {c}º valor: '))
    if val % 2 == 0:
        valores[0].append(val)
    else:
        valores[1].append(val)
valores[0].sort()
valores[1].sort()
print('=-' * 30)
print(f'Os valores pares escritos foram: {valores[0]}')
print(f'Os valores ímpares escritos foram: {valores[1]}')

