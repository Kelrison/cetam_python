# GABARITO - CRUD DO SISTEMA DE BIBLIOTECA
# Prof. Esp. Kelrison Coêlho
#
# Conteúdos utilizados:
# lista, lista de listas, while, for, if/elif/else,
# input(), append(), remove() e break.
#
# Observação:
# Este é um gabarito de referência. O aluno pode organizar
# o código de outra forma, desde que mantenha as funcionalidades
# solicitadas e consiga explicar seu funcionamento.


# Lista principal que armazenará todos os livros.
biblioteca = []


while True:

    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")


    # ==========================================================
    # CREATE - CADASTRAR
    # ==========================================================
    if opcao == "1":

        codigo = int(input("Código do livro: "))

        # Verifica se o código já existe na biblioteca.
        existe = False

        for livro in biblioteca:
            if livro[0] == codigo:
                existe = True

        if existe:
            print("Código já cadastrado!")
        else:

            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de publicação: "))

            # Cada livro é representado por uma lista.
            livro = [codigo, titulo, autor, ano]

            # Adiciona o livro à lista principal.
            biblioteca.append(livro)

            print("Livro cadastrado com sucesso!")


    # ==========================================================
    # READ - LISTAR
    # ==========================================================
    elif opcao == "2":

        if len(biblioteca) == 0:
            print("Nenhum livro cadastrado.")

        else:

            # O for percorre todos os livros da biblioteca.
            for livro in biblioteca:

                print("----------------------------")
                print("Código:", livro[0])
                print("Título:", livro[1])
                print("Autor:", livro[2])
                print("Ano:", livro[3])


    # ==========================================================
    # READ - PESQUISAR
    # ==========================================================
    elif opcao == "3":

        codigo_busca = int(input("Digite o código do livro: "))

        encontrado = False

        # Procura o livro pelo código.
        for livro in biblioteca:

            if livro[0] == codigo_busca:

                print("\nLivro encontrado!")
                print("Código:", livro[0])
                print("Título:", livro[1])
                print("Autor:", livro[2])
                print("Ano:", livro[3])

                encontrado = True

        if encontrado == False:
            print("Livro não encontrado.")


    # ==========================================================
    # UPDATE - ALTERAR
    # ==========================================================
    elif opcao == "4":

        codigo_busca = int(input("Digite o código do livro: "))

        encontrado = False

        # Localiza o livro antes de alterar seus dados.
        for livro in biblioteca:

            if livro[0] == codigo_busca:

                print("\nLivro encontrado.")

                # O código permanece o mesmo.
                livro[1] = input("Novo título: ")
                livro[2] = input("Novo autor: ")
                livro[3] = int(input("Novo ano de publicação: "))

                encontrado = True

                print("Livro alterado com sucesso!")

        if encontrado == False:
            print("Livro não encontrado.")


    # ==========================================================
    # DELETE - EXCLUIR
    # ==========================================================
    elif opcao == "5":

        codigo_busca = int(input("Digite o código do livro: "))

        encontrado = False

        # Procura o livro que será excluído.
        for livro in biblioteca:

            if livro[0] == codigo_busca:

                print("\nLivro encontrado:", livro[1])

                confirmacao = input("Deseja excluir? (S/N): ")

                if confirmacao.upper() == "S":

                    # Remove da biblioteca o livro encontrado.
                    biblioteca.remove(livro)

                    print("Livro excluído com sucesso!")

                else:
                    print("Exclusão cancelada.")

                encontrado = True

                # Como o código é único, não precisamos continuar.
                break

        if encontrado == False:
            print("Livro não encontrado.")


    # ==========================================================
    # SAIR
    # ==========================================================
    elif opcao == "6":

        print("Sistema encerrado.")

        # Encerra o while.
        break


    # ==========================================================
    # OPÇÃO INVÁLIDA
    # ==========================================================
    else:

        print("Opção inválida!")
