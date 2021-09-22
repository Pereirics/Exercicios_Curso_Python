cla = 'Sporting', 'Porto', 'Benfica', 'Braga', 'Paços de Ferreira', 'Santa Clara', 'Vitória SC', 'Moreirense', 'Famalicão', 'B-SAD', 'Gil Vicente', 'Tondela', 'Boavista', 'Portimonense', 'Marítimo', 'Rio Ave', 'Farense', 'Nacional'
print('-=' * 17)
print(f'Lista das equipas da Primeira Liga: {cla}')
print('-=' * 17)
print(f'Os 5 primeiros são: {cla[:5]}')
print('-=' * 17)
print(f'Os 4 últimos são: {cla[14:]}')
print('-=' * 17)
print(f'Equipas por ordem alfabética: {sorted(cla)}')
print('-=' * 17)
print(f'O Sporting está na {cla.index("Sporting") + 1}ª posição!')


