import random
first=[]
def sorteia (first):
    for c in range (0,5):
     first.append(random.randint(1,10))
    return first


def somapar (lista):
    soma=[]
    resultado=[]
    for c in range (len(lista)):
        if lista[c]  % 2 == 0:
            soma.append(lista[c])
    resultado.append(sum(lista))
    return resultado



numero=[]
num=sorteia(numero)
fim=somapar(num)
print(fim)
