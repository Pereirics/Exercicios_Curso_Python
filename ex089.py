lista = [[], [], []]
while True:
    lista[0].append(str(input('Nome: ')))
    lista[1].append(float(input('Nota 1: ')))
    lista[2].append(float(input('Nota 2: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for c in range(0, len(lista[0])):
    print(f'{c:<4}', end='')
    print(f'{lista[0][c]:<10}', end='')
    print(f'{(lista[1][c] + lista[2][c]) / 2:>8.1f}')
print('-' * 30)
n = int(input('Mostrar notas de qual aluno? (999 termina): '))
while n != 999:
    print(f'Notas de {lista[0][n]} são [{lista[1][n]},{lista[2][n]}]')
    print('-' * 30)
    n = int(input('Mostrar notas de qual aluno? (999 termina): '))
print('TERMINANDO...')
print('Volte Sempre!')

