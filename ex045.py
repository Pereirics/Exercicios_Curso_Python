import random
print('Bem-vindo ao jogo do "Pedra, Papel e Tesoura"!')

user = str(input('Escolha qual você quer jogar: ')).strip().lower()

cpu = random.choice(['pedra','papel','tesoura'])

if user == 'papel' and cpu == 'papel':
    print(f'O CPU escolheu {cpu}!')
    print('É um EMPATE!')
elif user == 'papel' and cpu == 'pedra':
    print(f'O CPU escolheu {cpu}!')
    print('O Utilizador venceu! Parabéns!')
elif user == 'papel' and cpu == 'tesoura':
    print(f'O CPU escolheu {cpu}!')
    print('O CPU venceu! Mais sorte para a próxima ;D')
elif user == 'pedra' and cpu == 'pedra':
    print(f'O CPU escolheu {cpu}!')
    print('É um EMPATE!')
elif user == 'pedra' and cpu == 'tesoura':
    print(f'O CPU escolheu {cpu}!')
    print('O Utilizador venceu! Parabéns!')
elif user == 'pedra' and cpu == 'papel':
    print(f'O CPU escolheu {cpu}!')
    print('O CPU venceu! Mais sorte para a próxima ;D')
elif user == 'tesoura' and cpu == 'tesoura':
    print(f'O CPU escolheu {cpu}!')
    print('É um EMPATE!')
elif user == 'tesoura' and cpu == 'papel':
    print(f'O CPU escolheu {cpu}!')
    print('O Utilizador venceu! Parabéns!')
elif user == 'tesoura' and cpu == 'pedra':
    print(f'O CPU escolheu {cpu}!')
    print('O CPU venceu! Mais sorte para a próxima ;D')
else:
    print('Escolha inválida! Siga as regras ;)')