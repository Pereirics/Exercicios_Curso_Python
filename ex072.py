num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',  'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte'

while True:
    while True:
        n1 = int(input('Insira um número de 0 a 20: '))
        if n1 in range(0,21):
            break
        print('Tente novamente. ', end='')
    for c in range(0,len(num)):
        if n1 == c:
            print(f'O número que escolheu foi o {num[c]}!')
    n2 = str(input('Pretende continuar? [S/N] ')).upper().strip()[0]
    if n2 in 'Nn':
        break
