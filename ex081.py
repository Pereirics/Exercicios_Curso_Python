lista = [int(input('Escreva um número: '))]
cont = 1
cont5 = 0
while True:
    continuar = str(input('Pretende continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    a = int(input('Escreva um número: '))
    lista.append(a)
    cont += 1
print('-=' * 30)
print(f'Você escreveu {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')



