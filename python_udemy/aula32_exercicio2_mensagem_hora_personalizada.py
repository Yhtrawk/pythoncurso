print("Que horas são? Digite apenas 2 dígitos")
hora = int(input())

if hora >= 0 and hora <= 11:
    print("Bom dia")
elif hora >= 12 and hora <= 17:
    print("Boa tarde")
elif hora >= 18 and hora <= 24:
    print("Boa noite")
else:
    print("Hora inválida")