def lista():
    numeros = []
    print("informe 15 numeros")
    for i in range(15):
        numeros.append(int(input("")))
        a=max(numeros)
    print("Maior numero informado:",a)
    print("Posição:",numeros.index(a))
lista()