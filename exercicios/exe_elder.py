def media_idades(pesos,idades):
    soma_idades = 0
    media_idades1 = soma_idades / 7
    peso = 0
    peso_acima_90k = 0
    cont = 0
    while cont < 7 :
        if pesos [cont] > 90:
            peso_acima_90k = peso_acima_90k + 1
        soma_idades = soma_idades [cont]
        cont = cont + 1
    return media_idades1   
