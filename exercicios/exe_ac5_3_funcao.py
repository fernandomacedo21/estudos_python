def contar(sequencia_caracteres: str, caractere_busca: str):
    cont = 0

    for i in range(0, len(sequencia_caracteres), 1):
        if sequencia_caracteres[i] == caractere_busca:
            cont = cont + 1

    return cont
