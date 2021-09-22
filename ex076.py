print('-' * 40)
print(' ' * 11, 'LISTA DE PREÇOS')
print('-' * 40)

n = 'Lápis', 1.25, 'Leite',2, 'Maçã', 0.25, 'Livro', 17.99, 'Compasso', '10'

for c in range(0,len(n),2):
    print(f'{n[c]:.<30}€ {n[c+1]:>7}')

