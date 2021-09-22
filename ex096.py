def area():
    print('Controle de Terrenos')
    print('-' * 30)
    a = float(input('Largura (m): '))
    b = float(input('Comprimento (m): '))
    ar = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {ar:.1f}m².')


area()
