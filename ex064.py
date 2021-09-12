cont = soma = 0

n1 = int(input('Escreva um número (999 para parar): '))

while n1 != 999:
    cont += 1
    soma += n1
    n1 = int(input('Escreva um número (999 para parar)                              : '))



print(f'No total foram escritos {cont} números e a soma entre eles dá {soma}!')
