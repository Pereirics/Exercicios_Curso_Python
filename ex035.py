n1 = float(input('Insira a medida de um dos lados do triângulo: '))
n2 = float(input('Insira a medida de outro lado do triângulo: '))
n3 = float(input('Insira a medida do último lado do triângulo: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Essas medidas podem formar um triângulo!')
else:
    print('Essas medidas não podem formar um triângulo!')
