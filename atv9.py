def menorq(lista):
    menores = []
    for num in lista:
        if num < 10:
            menores.append(num)
    return print (menores)
menorq([8,3,4,5,12,15,8,6,9])