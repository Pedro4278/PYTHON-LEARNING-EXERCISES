import random as sort

#crie um programa que gere 5 numeros aleatorios e os coloque em uma tupla (ok!)
cont=0
tupla=0
v=0
n1=0
n2=0
n3=0
n4=0
n5=0
for c in range(0,5):
 cont+=1
 v=sort.randint(0,20)
 if cont == 1:
    n1 = v
 if cont == 2:
    n2 = v
 if cont == 3:
    n3 = v
 if cont == 4:
    n4 = v
 if cont == 5:
    n5 = v
 if cont == 5:
  tupla=(n1,n2,n3,n4,n5)
  print(f'Os valores foram: {tupla}')
  t=sorted(tupla)
  menor=(t[0])
  maior=(t[4])
  print(f'O menor numero da tupla é {menor} e o maior é {maior}.')


