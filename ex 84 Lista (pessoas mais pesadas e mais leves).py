# Usando lista dizer:
# A pessoa mais pesada
# A pessoa mais leve

final=[]
tempo=[]
maior=menor=0
while True:
    tempo.append(input('nome: '))
    v=tempo.append(float(input('Peso:')))
    stop=input('Deseja parar? [s/n]')

    if maior == 0 and menor == 0:
        menor=maior=tempo[1]
    else:
        if tempo[1] < menor:
            menor=tempo[1]
        if tempo[1] > maior:
            maior=tempo[1]
    #não esqueça de deixar o clear por ultimo
    final.append(tempo[:])
    tempo.clear()


# 1 'p' de range == ['A sub lista que foi inserida'], ele vai passar por uma sublista de cada vez
    if stop == 's':
        for p in final:
            if p[1] == maior:
                print(f'Esta é a pessoa mais pesada: {p[0]} pesando {p[1]} kg.')
            elif p[1] == menor:
                print(f'Esta é a pessoa mais leve: {p[0]} pesando {p[1]} kg ')
        break

print(f'Você cadastrou {len(final)} pessoas')

