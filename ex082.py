lista = []
listaP = []
listaI = []

while True:
    inp = int(input('Escreva um número: '))
    if inp % 2 == 0:
        listaP.append(inp)
        lista.append(inp)
    else:
        listaI.append(inp)
        lista.append(inp)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaP}')
print(f'A lista de ímpares é {listaI}')