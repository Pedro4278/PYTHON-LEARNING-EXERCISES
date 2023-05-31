per=0
cont=0
media=0
first=[]
sec=[]
while per != 'n':
  cont+=1
  print(f'Cadastre o {cont}° aluno')
  nome=input('Nome: ')
  nota1=float(input("Nota 1° bimestre: "))
  nota2=float(input("Nota 2° bimestre: "))
  per=input('Deseja continuar [S/N]: '.lower())
  media = (nota1 + nota2) /2
  first.append(nome)
  first.append(nota1)
  first.append(nota2)
  first.append(media)
  sec.append(first[:])
  del first[:]

print('-='*30)
print('-'*15, 'MEDIA DOS ALUNOS','-'*15)
for c, aluno in enumerate(sec):
    print(f'indice: {c} nome: {sec[c][0]} media: {sec[c][3]}')
print('Para saber mais detalhes digite o indice do aluno')
indice=0
fim=0
while fim != 'fim':
    print('-='*50)
    indice=int(input('digite o indice:'))
    enumerate(sec)
    print(sec[indice])
    fim=input("Para encerra digite 'fim', se não aperte 'enter': ")

print('-='*15, 'FOI PRAZER TE AJUDAR! VOLTE SEMPRE', '-='*15)