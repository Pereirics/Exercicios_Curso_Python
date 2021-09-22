matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Escreva um valor para [{l},{c}]: '))
        matriz[l].append(valor)
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='') #o :^5 define o espaço a ter dentro
    print()
