from datetime import date

n1 = int(input('Escolha um ano ou escreva 0 para analisar o ano atual: '))

if n1 == 0:
    n1 = date.today().year

if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')