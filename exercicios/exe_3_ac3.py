n= int(input())
soma=0
cont=1

while cont <= n:
    solucao= 1 / (cont**2)
    soma=soma+solucao
    cont= cont + 1
print ("{:.6f}".format(soma))    
    
