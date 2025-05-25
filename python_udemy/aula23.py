# Operadores in e not in
# Strings são iteráveis (Da para navegar item por item nelas)
#  0 1 2 3
#  L u i z
# -4-3-2-1
nome = 'Luiz'
# print(nome[2])
# print(nome[-2])
# print(10 * '-')
# print('u' in nome)
# print('a' in nome)
# print(10 * '-')
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
