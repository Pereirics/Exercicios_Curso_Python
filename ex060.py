n1 = int(input('Escolha um número para descobrir o seu faatorial: '))
n = n1-1
while n != 1:
    n1 = n1 * n
    n -= 1

print(f'O fatorial do número escolhido é: {n1}!')
