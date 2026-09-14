print("=================================")
print("       SISTEMA PARA BIBLIOTECA")
print("=================================")

for tentativa in range(5):

    print()
    print("1 - Cadastrar Livros")
    print("2 - Cadastrar Alunos")
    print("3 - Realizar Empréstimo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        quantidade = int(input("Quantos livros deseja cadastrar? "))

        for i in range(quantidade):

            print()
            print("----- LIVRO", i + 1, "-----")

            codigo = int(input("Código do livro: "))
            titulo = input("Título do livro: ")
            autor = input("Nome do autor: ")
            ano = int(input("Ano de publicação: "))
            quantidade_disponivel = int(input("Quantidade disponível: "))

            if titulo == "":
                print("Título não informado.")
            elif autor == "":
                print("Autor não informado.")
            elif ano <= 0:
                print("Ano inválido.")
            elif quantidade_disponivel <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                print("Livro cadastrado com sucesso!")

    elif opcao == 2:

        quantidade = int(input("Quantos alunos deseja cadastrar? "))

        for i in range(quantidade):

            print()
            print("----- ALUNO", i + 1, "-----")

            matricula = int(input("Matrícula: "))
            nome = input("Nome do aluno: ")
            turma = input("Turma: ")

            if matricula <= 0:
                print("Matrícula inválida.")
            elif nome == "":
                print("Nome não informado.")
            elif turma == "":
                print("Turma não informada.")
            else:
                print("Aluno cadastrado com sucesso!")

    elif opcao == 3:

        print()
        print("----- EMPRÉSTIMO -----")

        codigo = int(input("Código do livro: "))
        matricula = int(input("Matrícula do aluno: "))
        quantidade_disponivel = int(
            input("Quantidade disponível do livro: ")
        )

        if codigo <= 0:
            print("Código do livro inválido.")
        elif matricula <= 0:
            print("Matrícula inválida.")
        elif quantidade_disponivel <= 0:
            print("Não é possível realizar o empréstimo.")
            print("Não há exemplares disponíveis.")
        else:
            print("Empréstimo realizado com sucesso!")

    elif opcao == 4:

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")