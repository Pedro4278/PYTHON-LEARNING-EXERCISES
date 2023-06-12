#crie uma função que calcule o valor de um terreno


def calcular (a,b):
    r= a * b
    return r

lista=[]


a=int(input('Digite a largura: '))
b=int(input('Digite o comprimento: '))

resultado=calcular(a,b)
print(f'A metragem do terreno é {resultado} m²')




