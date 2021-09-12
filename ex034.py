n1 = float(input('Qual é o seu salário? '))

if n1 < 1250:
    sal = n1 * 1.15
else:
    sal = n1 * 1.1

print(f'O seu novo salário tem o valor de {sal :.2f}€!')