nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
altura = float(input("Informe sua altura:"))

print ("O nome informado foi:", nome)
print ("A idade informada foi:", idade)
print ("A altura informada foi:", altura)
print (f"A altura informada foi: {nome}")


if idade >= 18:
    print("Voto obrigatório")
else:
    print("Voto NÃO obrigatório")
