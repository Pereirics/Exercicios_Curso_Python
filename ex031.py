n1 = float(input('Quantos kilómetros é a sua viagem? '))

if n1 > 200:
    custo = n1 * 0.45
else:
    custo = n1 * 0.50
print(f'A sua viagem irá custar: {custo :.2f}€!')
