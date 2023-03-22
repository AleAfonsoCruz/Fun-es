def impares(lista):
    impar = []
    for i in lista:
        if i % 2 != 0:
            impar.append(i)
    return print(impar)
impares([8,69,28,74,63,87,12,41])