#Declaração de variáveis, conversão e entrada de dados
#pelo usuário
nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
altura = float(input("Informe sua altura:"))

#Implementação 01
print ("O nome informado foi:", nome)
print ("A idade informada foi:", idade)
print ("A altura informada foi:", altura)
print (f"A altura informada foi: {nome}")

<<<<<<< Updated upstream

if idade >= 18:
    print("Voto obrigatório")
else:
    print("Voto NÃO obrigatório")
=======
#Implementação 02
print(f"O nome informado foi:{nome}")

if idade >= 18:
    print("Voto Obrigatório!")
else:
    print("Voto NÃO Obrigatório!")

#Implementação 02
>>>>>>> Stashed changes
