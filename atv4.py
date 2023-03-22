def pares(lista):
    par = []
    for p in lista:
        if p % 2 == 0:
            par.append(p)
    return print(par)
pares([8,56,97,41,25,5,12,15,35,48])