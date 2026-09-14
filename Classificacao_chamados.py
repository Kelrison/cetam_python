print("1 - Indisponível... ")
print("2 - Lentidão... ")
print("3 - Nao impede...")
print("4 - Outros...")
tipo_problema = int(input("Informe o tipo de problema: "))

if tipo_problema == 1:
    print("Critica")
elif tipo_problema == 2:
    print("Alta")
elif tipo_problema == 3:
    print("Média")
elif tipo_problema == 4:
    print ("Baixa")
else:
   print ("Opção Inválida!Presta atenção...") 