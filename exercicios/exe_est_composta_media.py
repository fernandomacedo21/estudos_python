print = ("Digite suas 3 primeiras notas")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1+nota2+nota3)/3 
if (media) >= 6.0 :
    print ('Aluno Aprovado')
else:
    print ('Aluno Reprovado')
