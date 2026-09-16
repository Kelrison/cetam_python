Repetidor = 1

while Repetidor == 1:
    print("O Palmeiras não tem mundial")
    resposta = int(input("Ganhou Mundial de Clubes? 1 SIM ou 2 NÃO : "))
    if resposta == 2:
       print ("Tente novamente...\n")
    elif resposta == 1:
        print ("\nAté que enfim..")
        break
    else:
        print("Resposta inválida\n")
    