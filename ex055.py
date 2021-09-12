maior = 0
menor = 1000

for c in range(1,6):
    n1 = float(input('Qual é o seu peso? '))
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
print('---------------------')
print(f'O menor peso é: {menor}kg,\nE o maior é {maior}kg!')