n1 = int(input('Insira um número: '))

primo = 1

for c in range(1,10):
    if n1 % c == 0 and c != 1 and c != n1:
        primo = 0
        c = 10

if primo == 1:
    print(f'O número {n1} é primo!')
else:
    print(f'O número {n1} não é primo!')

