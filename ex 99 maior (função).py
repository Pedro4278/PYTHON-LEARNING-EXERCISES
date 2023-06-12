def maior(lista):
    maior = lista[0]  # Assume the first element is the largest
    for item in lista:
        if item > maior:
            maior = item
    return maior


numeros=[3,4,9,10]
lista=maior(numeros)
print(lista)

