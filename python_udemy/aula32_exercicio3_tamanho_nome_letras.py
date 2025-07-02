print("Qual o seu primeiro nome?")
nome = input()

if " " in nome:
    print("Apenas o primeiro nome")
elif len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal")
elif len(nome) > 6:
    print("Seu nome é longo")