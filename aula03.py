# Exemplo de conversão Texto -> Float 
numero1 = input("Digite o primeiro número:")
print(f"O numéro digitado foi:{numero1}")

numero2 = float(numero1)
print(f"O número conververtido para float é:{numero2}")

#Exemplo de If, Elif, Else
idade = 14
if idade >= 18:
    print("Voto Obrigatório!")
elif idade >= 16:
    print("Voto Facultativo!")
else:
    print("Não vota")