#digitar quantos valores quiser
#cadastrar os valores em uma lista
#Caso o numero já exista não cadastre
#no final printar a lista em ordem crescente

v=0
per=0
numeros=[]
while per != 'n':
    v=int(input('Digite o valor aqui: '))

    if v in numeros:
      print('Valor duplicado')
      pass
    else:
     numeros.append(v)
     print('Valor adicionado com sucesso!')
    per = input('Quer continuar? [s/n]: ')

numeros.sort()
print(numeros)