Alunos = ["João","Pedro","José","Maria"]

for contador in Alunos:
    print(contador)

AdicionarAlunos = int(input("Quantos Alunos deseja cadastrar?"))

for n in range (AdicionarAlunos):
    
    Alunos.append(input("Informe o nome do Aluno:"))

for i in Alunos:
    print(i)