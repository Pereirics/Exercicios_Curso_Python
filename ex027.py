nome = str(input('Qual é o seu nome completo? ')).strip().split()
n2 = len(nome)
print(f'O seu primeiro nome é: {nome[0]}')
print(f'O seu último nome é: {nome[n2-1]}')

