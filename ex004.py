n = input('Escreva algo: ')

print(f'{n} é do tipo {type(n)}')
print(f'{n} é numérico? {n.isnumeric()}')
print(f'{n} é letra? {n.isalpha()}')
print(f'{n} é alfanumérico? {n.isalnum()}')
print(f'{n} é decimal? {n.isdecimal()}')
print(f'{n} só tem espaços? {n.isspace()}')
print(f'{n} está em maiúsculas? {n.isupper()}')
print(f'{n} está em minúsculas? {n.islower()}')
print(f'{n} está capitalizado? {n.istitle()}')