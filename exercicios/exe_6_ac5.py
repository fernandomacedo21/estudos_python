sair = False
pedidos = []

while not sair:
    opcao = input()
    if opcao == 'ajuda':
        print('''-----------------------------------
Pizzaria 0.1 - menu de comandos
-----------------------------------
- ajuda: exibe o menu de ajuda
- sair: encerra o programa
- exibir: exibe a lista de pedidos
- novo #pedido: adiciona o #pedido
- cancela #pedido: remove o #pedido
-----------------------------------''')
    elif opcao == 'sair':
        sair = True
    elif opcao == 'exibir':
        if len(pedidos) == 0:
            print('sem pedidos')
        else:
            texto = pedidos.__str__().replace("', '", " ")
            texto = texto.__str__().replace("['", "")
            texto = texto.__str__().replace("']", "")
            print(texto)

    elif opcao.__contains__('novo'):
        pedidos.append(opcao.split(' ')[1])
        print('pedido {} adicionado'.format(opcao.split(' ')[1]))
    elif opcao.__contains__('cancela'):
        item = opcao.split(' ')[1]
        if pedidos.__contains__(item):
            pedidos.remove(item)
            print('pedido {} removido'.format(item))
        else:
            print('pedido {} inexistente'.format(item))
