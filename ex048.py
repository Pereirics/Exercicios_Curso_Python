soma = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
print(f'A soma de todos os números ímpares que são múltiplos de 3 e que se encontram entre 1 e 500 dá: {soma}!')