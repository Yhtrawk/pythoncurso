"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
print("Por favor, digite seu nome a seguir: ")
nome = input()
print("Por favor, digite sua idade a seguir: ")
idade = input()

if nome and idade:
    print ("Seu nome é " + nome)
    print ("Seu nome invertido é " + nome[::-1])
    if " " in nome:
        print ("Seu nome contém espaços")
    else:
        print ("Seu nome não contém espaços")
    print ("Seu nome tem " + str(len(nome)) + " letras")
    print ("A primeira letra do seu nome é " + (nome[0]))
    print ("A última letra do seu nome é " + (nome[-1]))
else:
    print ("Desculpe, você deixou campos vazios.")
