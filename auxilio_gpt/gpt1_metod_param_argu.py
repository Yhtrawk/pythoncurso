# Aqui a gente cria um método chamado falar
def falar(mensagem):  # 'mensagem' é o PARÂMETRO (a caixinha)
    print("O robô disse:", mensagem)

# Agora vamos usar o método e dar uma frase pro robô dizer:
falar("Oi, humano!")  # "Oi, humano!" é o ARGUMENTO (o que vai dentro da caixinha)

# ↓↓↓ MÉTODO (ou função) chamado "calcular_frete"
def calcular_frete(distancia, vip):  # ← PARÂMETROS: distancia e vip
    if vip:
        return distancia * 0.5  # desconto para cliente VIP
    else:
        return distancia * 1.0  # valor normal

# ↓↓↓ CHAMANDO O MÉTODO com ARGUMENTOS: 30 e True
valor = calcular_frete(30, True)

print(f"Valor do frete: R$ {valor:.2f}")

#Me
'''
como se o método fosse uma ordem, 
"Aperte aquelas porcas na máquina", 
o Parâmetro fosse a maleta de ferramentas, 
e o argumento fosse as chaves inglesas 6 e 8
 q vc vai precisar pra usar na máquina, é isso?
'''

#ChatGPT
'''
Método → A ordem: "Aperte aquelas porcas na máquina"
→ Isso é o que deve ser feito (a função em si).

Parâmetros → A maleta de ferramentas com espaços vazios pra você colocar as ferramentas que serão usadas.
→ São os lugares reservados (como distancia, vip) que o método espera receber.

Argumentos → As ferramentas reais que você coloca na maleta: chave 6 e 8
→ São os valores reais que entram quando você chama o método (como 30, True).


'''

def apertar_porcas(chave1, chave2):  # parâmetros = espaços na maleta
    print(f"Apertando com a {chave1} e a {chave2}")

apertar_porcas("chave 6", "chave 8")  # argumentos = ferramentas reais
