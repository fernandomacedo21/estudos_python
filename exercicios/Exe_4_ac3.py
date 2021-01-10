n=int(input())

soma = 0
cont = 1
while cont<=n:
   calc_fracoes = 1/cont
   
   if cont % 2==0:
       soma = soma + calc_fracoes
   else:
      soma = soma - calc_fracoes 

   cont= cont + 1
      
    
print ("{:.6f}".format(soma))    
