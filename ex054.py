from datetime import date
cont = 0
for c in range(0,7):
    n1 = int(input('Qual é o seu ano de nascimento? '))
    if date.today().year - n1 >= 18:
        cont += 1
print(f'Das 7 pessoas que inseriram o seu ano de nascimento, {7 - cont} ainda não atingiram a maior idade e {cont} já atingiram a maior idade!')
