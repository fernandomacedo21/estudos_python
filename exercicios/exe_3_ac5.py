from exercicios.exe_ac5_3_funcao import *

texto = str(input())
caractere = str(input())

ocorrencias = contar(texto,caractere)

if ocorrencias >= 1:
    print('O caractere buscado ocorre',ocorrencias,'vezes na sequencia.')
else:
    print('Caractere nao encontrado.')