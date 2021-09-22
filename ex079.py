lista = [int(input('Escreva um valor: '))]

while True:
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'nN':
        break
    a = int(input('Escreva um valor: '))
    cont = 0
    for c in lista:
        if a != c and cont == 0:
            lista.append(a)
            print('Valor adicionado com sucesso...')
            break
        else:
            print('Valor duplicado! Não vou adicionar...')
        cont += 1

print('=-' * 30)
print(f'Você escrevou os valores {lista}')


