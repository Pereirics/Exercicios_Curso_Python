n2 = int(input('Insira um número: '))
cont = 1
soma = menor = maior = media = n2
n1 = input(str('Pretende continuar a inserir valores? [S/N] ')).upper().strip()[0]

while n1 in 'Ss':
    n2 = int(input('Insira um número: '))
    soma += n2
    cont += 1
    media = soma / cont
    if n2 > maior:
        maior = n2
    if n2 < menor:
        menor = n2
    n1 = input(str('Pretende continuar a inserir valores? [S/N] ')).upper().strip()[0]
    if n1 != 'S' and n1 != 'N':
        while n1 != 'S' and n1 != 'N':
            print('Escolha inválida, tente novamente!')
            n1 = str('Pretende continuar a inserir valores? [S/N] ')
print(f'O menor valor lido foi o {menor},\no maior foi o {maior}\ne a média de todos os números foi {media :.2f}! ')