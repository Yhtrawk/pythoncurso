"""
Fatiamento de strings
012345678 (Positivo, esq. pra dir., começa pelo zero)
Olá mundo
-987654321 (Negativo, dir. pra esq., começa pelo -1)
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[4:8])
print(variavel[-8:-2])
print(variavel[3])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[0:9:-1])
print(variavel[-1:-10:-1])