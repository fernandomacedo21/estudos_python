salario=float(input())
v1=1751.81
v2=2919.72
v3=5839.45
v4=v3*0.11
if salario<=v1:
    print('Desconto do INSS: R${:.2f}'.format(salario*0.08,2))
if salario>v1 and salario<=v2:
    print('Desconto do INSS: R${:.2f}'.format(salario*0.09,2))
if salario>v2 and salario<=v3:
    print('Desconto do INSS: R${:.2f}'.format(salario*0.11,2))
if salario>v3:
    print('Desconto do INSS: R${:.2f}'.format(v4,2))
