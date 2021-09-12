soma = 0
contIdade = 0
idadeVelho = 0
nomeVelho = ''

for c in range(1,5):
    print(f'-----{c}º PESSOA-----')
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é a sua idade? '))
    sexo = int(input('Qual é o seu sexo? Use 0 para masculino e 1 para feminino: '))
    soma += idade
    if sexo == 1:
        if idade < 20:
            contIdade += 1
    if idade > idadeVelho and sexo == 0:
        nomeVelho = nome
media = soma / 4

print(f'A média de idade no grupo é de {media :.2f} anos,\nO nome do homem mais velho é {nomeVelho} e,\n{contIdade} mulheres tem menos de 20 anos!')