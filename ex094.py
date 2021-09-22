dados = []
soma = media = cont = 0
while True:
    pessoa = {'nome': str(input('Nome: '))}
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Responda apenas F ou M')
    pessoa['idade'] = int(input('Idade: '))
    dados.append(pessoa)
    while True:
        resp = str(input('Pretende continuar? [S/N] ')).strip().upper()[0]
        if resp in 'NS':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
for c in dados:
    cont += 1
    soma += c['idade']
    media = soma / cont
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for c in dados:
    if c['sexo'] in 'F':
        print(c["nome"], end=' ')
print('\nD) Lista das pessoas que estão acimda da média de idades:',end='')
for c in dados:
    if c['idade'] > media:
        print('\n    ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
print('\n<< ENCERRADO >>')




