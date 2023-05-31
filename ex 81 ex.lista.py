#Ler varios numeros
#Quantos numeros foram digitados
#valores em ordem decrescente
# Se o valor 5 foi digitado
numeros=[]
nume=0
v=0
while v != 'n':
    num=int(input('Digite um numero: '))
    v=input('Quer continuar?[s/n]: ')
    numeros.append(num)
    nume+=1
    numeros.sort(reverse=True)

print('-='*30)
print(f'Foram digitados {nume} numeros')
print('-='*30)
print(f'Estes são os valores em ordem decrescente: {numeros}')
print('-='*30)
if 5 in numeros:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')
print('-='*30)

