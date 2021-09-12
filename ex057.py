sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]

if sexo == 'M' or sexo == 'F':
    print('---FIM---')
else:
    while sexo not in 'MFmf':
        print('Resposta inválida, por favor tente novamente.')
        sexo = str(input('Qual é o seu sexo? [M/F] '))
    print('---FIM---')