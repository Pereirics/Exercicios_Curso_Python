jogador = {}
equipa = []
cont = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos jogou o {jogador["nome"]}? '))
    jogador['golos'] = []
    jogador['total'] = 0
    for c in range(0, jogos):
        a = int(input(f'  Quantos golos na partida {c + 1}? '))
        jogador['golos'].append(a)
        jogador['total'] = jogador['total'] + a
    equipa.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print('cod nome            golos            total')
print('-' * 60)
for c in equipa:
    print(f'{cont:>3} {c["nome"]:<15} {c["golos"]} {c["total"]:<10}')
    cont += 1
print('-' * 60)
while True:
    while True:
        mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if 0 <= mostrar < cont or mostrar == 999:
            break
        else:
            print('Erro! Valor inválido, tente novamente!')
    if mostrar == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {equipa[mostrar]["nome"]}:')
        for i, v in enumerate(equipa[mostrar]["golos"]):
            print(f'   No jogo {i + 1} fez {v} golos.')
        print('-' * 60)
print('--- VOLTE SEMPRE! ---')

