#Declaração de variáveis, conversão e entrada de dados
#pelo usuário
nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
altura = float(input("Informe sua altura:"))

#Implementação 01
print ("O nome informado foi:", nome)
print ("A idade informada foi:", idade)
print ("A altura informada foi:", altura)

#Implementação 02
print(f"O nome informado foi:{nome}")
print(f"A idade informada foi:{idade} ")
print(f"A altura informada foi:{altura}")

if idade >= 18:
    print("Voto Obrigatório!")
else:
    print("Voto NÃO Obrigatório!")

