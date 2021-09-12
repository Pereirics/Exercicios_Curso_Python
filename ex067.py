print('-' * 30)
while True:
    n1 = int(input('Quer ver a tabuada de que número? '))
    print('-' * 30)
    n2 = 1
    if n1 < 0:
        print('PROGRAMA TERMINADO, XAU!')
        break
    else:
        for n2 in range(1, 11):
            print(f'{n1} x {n2} = {n1*n2}')
        print('-' * 30)
