tupla = 'hamburguer', 'ola', ' adeus', 'aprender', 'programar', 'aprender', 'gratis', 'python'

for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
