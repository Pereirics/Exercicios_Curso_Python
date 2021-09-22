def notas(*num, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    print('-' * 30)
    dicio = {'total': len(num)}
    maior = menor = num[0]
    soma = 0
    for c in num:
        soma += c
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
    dicio['maior'] = maior
    dicio['menor'] = menor
    dicio['média'] = soma / len(num)
    if dicio['média'] < 8:
        sit = 'TERRÍVEL'
    elif 8 <= dicio['média'] < 10:
        sit = 'MÁ'
    elif 10 <= dicio['média'] < 14:
        sit = 'RAZOÁVEL'
    elif 14 <= dicio['média'] < 17:
        sit = 'BOA'
    else:
        sit = 'EXCELENTE'
    if situacao == True:
        dicio['situacao'] = sit
    return dicio


resp = notas(14,18,20,situacao=True)
print(resp)
help(notas)



