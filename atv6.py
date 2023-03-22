def strlonga(lista):
    maior = lista[0]
    for m in lista:
        if len(m) > len(maior):
            maior = m
    return print(maior)
strlonga (["Paralelepípedo", "otorrinolaringologista", "Hipopotomonstrosesquipedaliofobia", "motosserra"])