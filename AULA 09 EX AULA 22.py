

#print(emoji.emojize('Leitor de Nomes :smile:'))

v=input('Digite seu nome completo aqui ')
print('este nome em maiusculo fica {}'.format(v.upper()))
print('este nome em minusculo fica {}'.format(v.lower()))
div=(v.split())
#quantas letras no primeiro nome:
nome=(div[0])
print('o primeiro nome tem {} letras'.format(len(nome)))
#######
j=''.join(div)
print('este nome tem {} letras no total'.format(len(j)))










