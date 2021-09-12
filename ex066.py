cont = soma = 0
while True:
    n1 = int(input('Escreva um número (999 para parar o programa): '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'No total foram escritos {cont} números,\nA soma entre eles deu {soma}!')
