#Quantas vezes o 9 apareceu
#Em que posição foi digitado o primeiro 3
#Quais foram os numeros pares


todos=0
prime3=0
n5=0
n4=0
n3=0
n2=0
n1=0
cont=0
contpar=0
pares=[]
posi3=0
cont3=0
nove=0
for c in range(0,4):
    cont+=1
    v=int(input('Digte o valor aqui: '))
    if v == 3 and cont3 == 0:
        posi3 += c+1
        cont3+=1
    if v == 9:
        nove+=1


    if cont == 1:
        n1=v
    if cont == 2:
        n2=v
    if cont == 3:
        n3=v
    if cont == 4:
        n4=v
    if cont == 4:
     todos=[n1,n2,n3,n4]
     cont+=1

     for c in range(0,1):
      if cont == 5:
        # contpar+=1
         if todos[0] % 2 == 0 and contpar == 1:
             # print(todos[0])
             pares.append(todos[0])

        # contpar+=1
         if todos[1] % 2 == 0 and contpar == 2:
             # print(todos[1])
             pares.append(todos[1])
        # contpar+=1
         if todos[2] % 2 == 0 and contpar == 3:
             # print(todos[2])
             pares.append(todos[2])
        # contpar+=1
         if todos[3] % 2 == 0 and contpar == 4:
             # print(todos[3])
             pares.append(todos[3])
        # contpar+=1

if cont3==0:
 print('Você não digitou o numero 3')
elif cont3 > 0:
 print(f'Você inseriu o numero 3 na {posi3}° posição')

if len(pares)==0:
     print('Você não digitou numeros pares')
else:
    print(f'Dentre os numeros que você digitou esses são pares {pares}')

if nove > 0:
 print(f'Quantas vezes você digitou o numero nove: {nove}')
else:
    print('Você não digitou o numero 9')







