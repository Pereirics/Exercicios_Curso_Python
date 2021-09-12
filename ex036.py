print('Bem-vindo ao banco!')
valor = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende pagar a casa? '))

meses = anos * 12

prestacao = valor / meses

if prestacao > sal * 0.3:
    print('Lamento! O seu empréstico foi negado!')
else:
    print('Parabéns! O seu empréstimo foi aceite!')