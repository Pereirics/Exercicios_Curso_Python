lista = []
for c in range(0,5):
    a = int(input('Escreva um número: '))
    if c == 0 or a > lista[-1]:
        lista.append(a)
    else:
        pos = 0
        while pos < len(lista):
            if a <= lista[pos]:
                lista.insert(pos, a)
                break
            pos += 1

print('-=' * 30)
print(f'Os valores escritos em ordem foram {lista}')
