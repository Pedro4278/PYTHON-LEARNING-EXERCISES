par=[]
impar=[]
todos=[]
for num in range (7):
    todos.append(int(input('Digite o Numero aqui: ')))

for cada in todos:
    if cada % 2 == 0:
       par.append(cada)
    elif cada % 2 != 0:
     impar.append(cada)

impar.sort()
par.sort()

print(f'Estes são os numeros pares: {par}' )
print(f'Estes são os numeros impares: {impar}' )