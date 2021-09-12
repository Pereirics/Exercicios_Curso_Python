#lê a idade de várias pessoas, no final de cada uma pergunta se pretende continuar
#No final mostra:
#Quantas pessoas tem + de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres tem - de 20 anos
contSexo = 0
contIdade = 0
contM = 0
print('-' * 30)
print('CADASTRAR UMA PESSOA')
print('-' * 30)

while True:
    n1 = n3 = ''
    while n1 != 'M' or n1 != 'F':
        n1 = str('Qual é o seu sexo? [M/F] ').strip().upper()
    n2 = int(input('Qual é a sua idade? '))
    if n1 == 'M':
        contSexo += 1
    if n1 == 'F' and n2 < 20:
        contM += 1
    if n2 >= 18:
        contIdade += 1
    while n3 != 'S' or n3 != 'N':
        n3 = str(input('Pretende continuar? [S/N] '))
    if n3 == 'N':
        break
