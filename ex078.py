lista= [int(input('Escreva um valor para a posição 0: '))]
maior = menor = lista[0]
maiorP = menorP = [0]
for c in range(1,5):
    lista.append(int(input(f'Escreva um valor para a posição {c}: ')))
    if lista[c] > maior:
        maior = lista[c]
        maiorP = [c]
    elif lista[c] < menor:
        menor = lista[c]
        menorP = [c]
    elif lista[c] == maior:
        maiorP.append(c)
    elif lista[c] == menor:
        menorP.append(c)

print('=-' * 30)
print(f'Você escreveu os valores: {lista}')
print(f'O maior valor escrito foi {maior} nas posições ',end='')
for c in maiorP:
    print(c,'...',end=' ')
print(f'\nO menor valor escrito foi {menor} nas posições ',end='')
for c in menorP:
    print(c,'...',end=' ')

