dicio = {'nome': str(input('Nome: '))}
dicio['media'] = float(input(f'Média de {dicio["nome"]}: '))
print('-=' * 30)
if dicio['media'] >= 9.5:
    dicio['situação'] = 'Aprovado'
elif 8 <= dicio['media'] < 9.5:
    dicio['situação'] = 'Recurso'
else:
    dicio['situação'] = 'Reprovado'
for k,v in dicio.items():
    print(f'A {k} é igual a {v}')



