def ocorrencia(lista, num):
    contador = 0
    for n in lista:
        if n == num:
            contador +=1
    return print (contador)
ocorrencia([8,8,5,7,4,1,2,3,9,9,9,9,9,6,5],9)