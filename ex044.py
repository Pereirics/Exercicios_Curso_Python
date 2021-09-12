pre = float(input('Qual o preço do produto que pretende comprar? '))
met = int(input("""Escolha um método de pagamento:
1 para dinheiro/cheque (10% de desconto)
2 para cartão de débito (5% de desconto)
3 para pagar em 2 prestações com cartão (0% juros)
4 para pagar em 3 ou mais prestações no cartão (20% juros)
Insira a opção: """))

if met == 1:
    pre = pre * 0.9
elif met == 2:
    pre = pre * 0.95
elif met == 4:
    pre = pre * 1.2

print(f'O preço com a opção escolhida é de {pre}€!')