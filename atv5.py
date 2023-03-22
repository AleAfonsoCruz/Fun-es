def palavras(lista):
    a = []
    for palavra in lista:
        if palavra[0] == "a" or palavra[0] == "A":
            a.append(palavra)
    print(a)
palavras (["avião", "Amor", "algoritmo", "Coruja", "Estranho", "Pepsi", "Triângulo", "escolha"])