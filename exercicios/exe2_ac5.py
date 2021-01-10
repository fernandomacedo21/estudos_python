pedir_numero = True

while pedir_numero :
    n1 = int(input())
    if n1 >=1 and n1<=9 :
        while pedir_numero:
            n2 = int(input())
            if n2 >=1 and n2<=9 :
               pedir_numero = False
            else:
                print('Insira um número final entre 1 e 9')
    else:
        print('Insira um número inicial entre 1 e 9')

if n1 > n2:
        print('Nenhuma tabela nesse intervalo')


for tab in range (n1,n2+1):
    for num in range (1,10):

        print('{} x {} = {}'.format(tab,num, num*tab))
    print('')

