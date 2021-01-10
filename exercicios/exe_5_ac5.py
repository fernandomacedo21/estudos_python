digite_produto = True
contador = 0
itens = []
while digite_produto:
    item = input('').split(' ')

    if item[0] == '0':
        digite_produto = False
    else:
        itens.append([int(item[0]), float(item[1]), float(item[2]), (float(item[1]) * float(item[2]))])

if (len(itens) == 0):
    print('nao tem compras')
else:
    itens.sort(key=lambda x: x[3])
    index = len(itens) - 1
    print('Item mais caro')
    print('Codigo: {}'.format(itens[index][0]))
    print('Quantidade: {:.0f}'.format(itens[index][1]))
    print('Custo: {:.2f}'.format(itens[index][3]))
