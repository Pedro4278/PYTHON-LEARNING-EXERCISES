# Ler 5 valores numericos
#Arquivar em uma lista
# dizer qual o maior e o menor
# Qual a posição de cada um

indice=0
menor=0
maior=0
cont=0
posima=0
posime=0
for indice, num in enumerate(range(6)):
       v=int(input('Digite o numero aqui: '))
       cont+=1
       if cont == 1:
           maior = v
           menor = v
       if v > maior:
           maior=v
           posima=indice
       if v < menor:
           menor=v
           posime=indice
print(f'O maior numero é {maior} e apareceu na posição {posima+1}')
print(f'O menor numero é {menor} e apareceu na posição {posime+1}')