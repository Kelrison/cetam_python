#Começa em 10, termina em 0 e diminui -1 a cada volta do laço
for numero in range(10, 0, -1):
    print(numero)

print("Fim da contagem!")

#Verifica se o número ao ser dividido por 3 será igual a zero, logo, é múltiplo de 3.
for numero in range(1, 31):
    if numero % 3 == 0:
        print(numero)

#Variável soma irá acumular as notas informadas a cada volta do laço, no fim soma será dividida por 4
soma = 0

for i in range(4):
    nota = float(input("Digite a nota: "))
    soma = soma + nota

media = soma / 4

print("Média:", media)

# Recebe o nome de 5 produtos e imprime com mensagem de sucesso ao final :)
for i in range(5):
    produto = input("Digite o nome do produto: ")
    print("Produto", produto, "cadastrado com sucesso!")

print("Todos os produtos foram cadastrados.")