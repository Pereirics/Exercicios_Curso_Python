def ficha(nome='<desconhecido>', golos=0):
    print(f'O jogador {nome} fez {golos} golo(s) no campeonato.')


print('-' * 30)
nome1 = str(input('Nome do jogador: '))
golos1 = str(input('Número de golos: '))
if golos1.isnumeric():
    golos1 = int(golos1)
else:
    golos1 = 0
if nome1.strip() == '':
    ficha(golos=golos1)
else:
    ficha(nome1, golos1)

