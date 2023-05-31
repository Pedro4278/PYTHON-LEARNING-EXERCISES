print('\033[33;44m Indentificador de Letras \033[m')

#Quantos "A"s a sua frase tem
v=input('Digite aqui a sua frase ')
min=(v.count('a'))
mai=(v.count('A'))
print("A sua frase tem \033[34m {} \033[m letras 'a'".format(min))
print('A sua frase tem \033[33m {} \033[m letras "A"'.format(mai))

# Em qual posição ela aparece pela primeira vez:
pos1=(v.find('a'))
pos2=(v.find('A'))
print('A letra "a" aparece pela primeira vez na forma minuscula no microlocal \033[34m n° {} \033[m '.format(pos1))
print('A letra "A" aparece pela primeira vez na forma maiuscula no microlocal \033[33m n° {} \033[m '.format(pos2))

#Aonde a letra aparece por ultimo:
ult=(v.rfind('a'))
ult1=(v.rfind('A'))
print('A letra "a" aparece em minusculo pela ultima vez em \033[34m {} \033[m  '.format(ult))
print('A letra "A" aparece em maiusculo pela ultima vez em \033[33m  {} \033[m '.format(ult1))








