preco = float(input("Digite o preço:"))
quantidade = int(input("digite a quantidade:"))
total = preco*quantidade
if total > 150.00:
        print ("O Total de sua compra com desconto foi: " ,total * 0.9)
else:        
        print ("O total de sua compra foi: ", total)               
