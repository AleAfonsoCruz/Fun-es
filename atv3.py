def nummaior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
print(nummaior([7,9,12,10,5,8]))