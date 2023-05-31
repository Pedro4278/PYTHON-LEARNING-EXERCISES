
result=0
v=0
while v != 999:
  v=int(input('Digite um numero: '))
  if v==999:
     break
  result+=v
  cont += 1
print(f'Você digitou {cont} valores e o resultado da soma entre eles é {result}')