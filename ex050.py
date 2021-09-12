soma = 0
for c in range(1,7):
    n1 = int(input('Escreva um número: '))
    if n1 % 2 == 0:
        soma += n1
print(f'A soma entre os números pares que digitou tem o valor de {soma}!')
