termo = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a sua razão? '))
n = -1
n1 = 1

while n1 != 0:
    n1 = int(input('Quantos termos quer adicionar? '))
    if n1 == 0:
        print('---FIM---')
    else:
        while n != n1:
            print(f'{termo}')
            termo += razao
            n += 1
