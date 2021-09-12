termo = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão da PA? '))

print(termo)
for c in range(1,10):
    termo += razao
    print(termo)
