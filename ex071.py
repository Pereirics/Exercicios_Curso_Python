print('=' * 30)
print(' ' * 10, 'BANCO BCP')
print('=' * 30)

n = int(input('Quanto quer levantar? € '))

if n < 0:
    while n < 0:
        print('Valor incorreto! Tente novamente.')
        n = int(input('Quanto quer levantar? € '))
n50 = n // 50
n20 = n % 50 // 20
n10 = n % 50 % 20 // 10
n5 = n % 50 % 20 % 10 // 5
n1 = n % 50 % 20 % 10 % 5 // 1

print(f'Total de {n50} notas de 50€')
print(f'Total de {n20} notas de 20€')
print(f'Total de {n10} notas de 10€')
print(f'Total de {n5} notas de 5€')
print(f'Total de {n1} moedas de 1€')
print('--------OBRIGADO--------')
