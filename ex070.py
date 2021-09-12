print('-' * 30)
print(' ' * 6, 'LOJA DO BARATINHO')
print('-' * 30)

total = totalA = 0
menor = 9999999999
menorP = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: €'))
    total += preco
    if preco > 100:
        totalA += 1
    if preco <= menor:
        menor = preco
        menorP = nome
    c = str(input('Pretende continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi de {total:.2f}€')
print(f'Temos {totalA} produtos custando mais de 100€')
print(f'O produto mais barato foi {menorP} que custa {menor}€')

