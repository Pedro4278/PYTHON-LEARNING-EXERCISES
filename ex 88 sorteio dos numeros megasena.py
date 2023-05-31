import random

tempo=[]
jogos=[]
v=int(input('Quantos jogos você quer fazer: '))

for c in range (0,v):
 for c in range(6):
  num = random.randint(0,60)
  tempo.append(num)
  tempo.sort()

 if len(tempo) == 6:
     for c in range(5):
        if c < 5  and  tempo[c] == tempo[c + 1]:

            del tempo[c]
            novo = random.randint(0, 60)
            if novo in tempo:
             for sorteio in range (60):
                  novo=random.randint(0,60)
                  if novo in tempo:
                      pass

                  else:
                   tempo.insert(c,novo)
                   tempo.sort()
                   break
            else:
                tempo.insert(c,novo)
                tempo.sort()



 jogos.append(tempo[:])
 tempo.clear()

len(jogos)



print("-="*30)
cont=0
for c in jogos:
 cont+=1
 print(f'O {cont}° jogo é: {c}')
print('-='*15, 'BOA SORTE!', '=-'*15)

