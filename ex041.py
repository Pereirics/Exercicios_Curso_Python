from datetime import date

ano = date.today().year
idade = int(input('Em que ano nasceu? '))

if ano - idade <= 9:
    print('Categoria MIRIM')
elif ano - idade <= 14:
    print('Categoria INFANTIL')
elif ano - idade <= 19:
    print('Categoria JUNIOR')
elif ano - idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('MASTER')