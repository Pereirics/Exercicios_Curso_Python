n1 = float(input('Escreva um número:'))
n2 = float(input('Escreva outro número: '))
n3 = float(input('Escreva mais um número: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 <= n3:
        menor = n2
    else:
        menor = n3
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 <= n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n1 <= n2:
        menor = n1
    else:
        menor = n2

print(f'O menor é o {menor} e o maior é o {maior}!')