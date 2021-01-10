entrada = str(input()).split()

total_alunos = int(entrada[0])

numero_sorteado = int(entrada[1])

nome_alunos = []

while total_alunos > 0:
    nome_alunos.append(str(input()))
    total_alunos = total_alunos - 1

nome_alunos.sort()

print(nome_alunos[numero_sorteado-1])