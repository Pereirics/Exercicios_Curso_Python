n1 = int(input('Escreva um número: '))
m = int(input("""Escolha um método de conversão:
1 para binário
2 para octal
3 para hexadecimal
Insira o valor: """))

if m == 1:
    n1 = bin(n1)
elif m == 2:
    n1 = oct(n1)
elif m == 3:
    n1 = hex(n1)
else:
    print('Valor inválido!')

print(f'O valor convertido para a opção escolhida é: {n1}!')
