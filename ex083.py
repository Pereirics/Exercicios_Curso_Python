inp = str(input('Escreva uma expressão: ')).strip()
contAberto = contFechado = 0
for letra in inp:
    if letra == ')':
        contFechado += 1
        if contFechado > contAberto:
            break
    elif letra == '(':
        contAberto += 1
if contAberto != contFechado:
    print('A sua expressão está errada!')
else:
    print('A sua expressão está correta!')
