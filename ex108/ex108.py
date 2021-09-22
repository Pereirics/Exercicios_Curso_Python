from ex107 import moeda

n = float(input('Escreva o preço: '))
print(f'A metade de {moeda.moeda(n)}€ é {moeda.moeda(moeda.metade(n))}€')
print(f'O dobro de {moeda.moeda(n)}€ é {moeda.moeda(moeda.dobro(n))}€')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentarOuDiminuir(10, n))}€')
