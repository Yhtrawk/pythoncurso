primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor})')
elif segundo_valor > primeiro_valor:
    print(f'Segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor})')
else:
    print('Ambos os valores são iguais')
