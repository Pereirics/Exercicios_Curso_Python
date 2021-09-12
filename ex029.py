n1 = float(input('A que velocidade ia o seu carro? '))

if n1 > 80:
    multa = (n1 - 80) * 7
    print(f'EXCESSO DE VELOCIDADE! A multa é de {multa :.2f}€!')
else:
    print('Continuação de boa viagem!')

