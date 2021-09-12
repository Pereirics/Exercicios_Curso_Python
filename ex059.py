num1 = int(input('Escreva um número: '))
num2 = int(input('Escreva outro número: '))
n = 0

print("""----------MENU----------
   [1] Somar
   [2] Multiplicar
   [3] Maior
   [4] Novos números
   [5] Sair do programa
----------MENU----------""")

while n != 5:
    n = int(input('Insira a sua opção: '))
    if n == 1:
        print(f'A soma entre os dois dá {num1 + num2}!')
        print('-----------------------')
    elif n == 2:
        print(f'A multiplicação entre os dois dá {num1 * num2}')
        print('-----------------------')
    elif n == 3:
        if num1 > num2:
            print(f'O maior entre os dois é o {num1}')
            print('-----------------------')
        else:
            print(f'O maior entre os dois é o {num2}')
            print('-----------------------')
    elif n == 4:
        num1 = int(input('Escreva um número: '))
        num2 = int(input('Escreva outro número: '))
    elif n == 5:
        print('----------FIM----------')
    else:
        print('Opção inválida! Tente novamente!')
        print('-----------------------')

