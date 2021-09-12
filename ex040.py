n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1 + n2) / 2

if media >= 9.5:
    print('APROVADO!')
elif media < 9.5 and media >= 8:
    print('RECURSO!')
else:
    print('PARA O ANO HÁ MAIS!')