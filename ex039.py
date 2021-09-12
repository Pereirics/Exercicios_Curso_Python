from datetime import date

ano = date.today().year

idade = int(input('Em que ano nasceu? '))

if ano - idade < 18:
    print(f'Ainda não está na hora de se alistar, só daqui a {18-(ano-idade)} ano(s)!')
elif ano - idade == 18:
    print('Está na hora de se alistar! VAMOS AGORA!')
else:
    print(f'Já passou a sua vez por {ano-idade-18} anos! Estás safo ;D')
