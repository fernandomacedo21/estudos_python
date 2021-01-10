notaList = [6.0, 7.0, 5.0, 8.0]
i = 0
soma = 0
while i < len(notaList):
    print('Nota', i+1, '---> ', notaList[i])
    soma = soma + notaList[i]
    i = i + 1
print('média ---> ', soma/len(notaList))