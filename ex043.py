peso = float(input('Qual é o seu peso em Kg? '))
alt = float(input('Qual é a sua altura em metros? '))

imc = peso / (alt * alt)

if imc < 18.5:
    print('Está abaixo do peso! Tem que comer mais!')
elif imc <= 25:
    print('Está no peso ideal! mantenha-se assim!')
elif imc <= 30:
    print('Está no sobrepeso! Está na altura de começar a fazer exercício!')
elif imc <= 40:
    print('Está com obesidade! Consulte um médico para o ajudar!')
else:
    print('Está com OBESIDADE MÓRBIDA! VÁ A UM MÉDICO IMEDIATAMENTE!!!')
