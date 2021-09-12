n1 = str(input('Escreva um frase para testar se é um palíndromo: ')).replace(" ","").strip().lower()

comp = len(n1)
inverso = ''

for c in range(comp - 1, -1, -1):
    inverso += n1[c]

if n1 == inverso:
   print('Parabéns! A frase é um palíndromo!')
else:
   print('QUe pena, a palavra não é um palíndromo!')


