from random import randint

num = int(input('Tente adivinhar o número que o computador vai escolher entre 1 e 5: '))

num1 = randint(1,5)

if num == num1:
    print('Acertou! Parabéns!')
else:
    print(f'Errou! O número correto era o {num1}! Boa sorte para a próxima vez :D')
print('----------FIM----------')