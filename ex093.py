dados = {'nome': str(input('Nome do jogador: '))}
jogos = int(input(f'Quantos jogos jogou o {dados["nome"]}? '))
dados['golos'] = []
dados['total'] = 0
for c in range(0, jogos):
    a = int(input(f'  Quantos golos na partida {c}? '))
    dados['golos'].append(a)
    dados['total'] = dados['total'] + a
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {jogos} jogos.')
for i, v in enumerate(dados['golos']):
    print(f'  => Na partida {i}, fez {v} golos.')
print(f'Foi um total de {dados["total"]} golos.')
