num1 = int(input('entre com o valor inicial: '))
num2 = int(input('entre com o valor final: '))
soma =  0
for i in range (num1,num2 +1 ):
    if i % 2 == 0:
        soma =  soma + i
print (' A soma eh',soma)
