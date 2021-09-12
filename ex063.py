n = int(input('Quantos elementos da Sequência de Fibonacci quer ver? '))
temp1 = 0
temp2 = 1

if n == 1:
    print('0')
elif n == 2:
    print('0 -> 1')
else:
    print('0 -> 1 -> ',end='')
    n = n - 2
    while n != 0:
        temp = temp1
        temp1 = temp2
        temp2 = temp + temp2
        if n != 1:
            print(f'{temp2} -> ',end='')
        else:
            print(f'{temp2}')
        n = n - 1
