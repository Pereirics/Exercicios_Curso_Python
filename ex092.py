from datetime import datetime
dados = {'nome': str(input('Nome: '))}
nascimento = int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
dados['idade'] = datetime.now().year - nascimento

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: €'))
    dados['aposentadoria'] = dados['contratação'] - nascimento + 35
print('-=' * 30)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')


