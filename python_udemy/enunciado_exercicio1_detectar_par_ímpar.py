print("Digite um número inteiro: ")

try:
    numero_inteiro = int(input())

    if numero_inteiro % 2 == 0:
        print("Este número é par")
    elif numero_inteiro % 2 != 0:
        print("Este número é ímpar")

except ValueError:
    print("Você não digitou um número inteiro válido.")