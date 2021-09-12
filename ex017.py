from math import sqrt, pow

n1 = float(input('Insira o comprimento de um dos catetos: '))
n2 = float(input('Insira o comprimento do outro cateto: '))
print(f'O comprimento da hipotenusa é: {sqrt((pow(n1,2) + pow(n2,2))) :.2f}')
