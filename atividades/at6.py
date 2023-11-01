# Criando um dicionário vazio para armazenar os dados dos alunos
alunos = {}

# Realizando a leitura dos valores utilizando um loop
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

# Calculando a soma das notas
soma_notas = 0
for nota in alunos.values():
    soma_notas += nota

# Calculando a média das notas
media_notas = soma_notas / len(alunos)

print("Notas dos alunos:", alunos)
print("Média das notas:", media_notas)
