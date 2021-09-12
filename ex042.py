n1 = float(input('Insira a medida de um dos lados do triângulo: '))
n2 = float(input('Insira a medida de outro lado do triângulo: '))
n3 = float(input('Insira a medida do último lado do triângulo: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Essas medidas podem formar um triângulo!')
    if n1 == n2 == n3:
        print('O triângulo é equilátero!')
    elif n1 == n2 != n3:
        print('O triângulo é isósceles!')
    elif n1 != n2 == n3:
        print('O triângulo é isósceles!')
    elif n1 == n3 != n2:
        print('O triângulo é isósceles!')
    else:
        print('O triângulo é escaleno!')
else:
    print('Essas medidas não podem formar um triângulo!')
