matriz = [[],[],[]]
somaPares = somaTCol = MaiorSL = 0
for l in range(0,3):
    for c in range(0,3):
        val = int(input(f'Escreva o valor para [{l,c}]: '))
        matriz[l].append(val)
        if val % 2 == 0:
            somaPares += val
        if c == 2:
            somaTCol += val
        if c == 0 and l == 1:
            MaiorSL = val
        elif c != 0 and l == 1 and val > MaiorSL:
            MaiorSL = val
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTCol}.')
print(f'O maior valor da segunda linha {MaiorSL}.')