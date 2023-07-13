#Melhore o exercicio 107 criando uma função para formatar os numeros

import moeda_curso

t = int(input('Digite o valor da moeda: '))
p= int(input('Digite a porcentagem: '))

print(f'O dobro da moeda é {moeda_curso.edit(moeda_curso.dobro(t) )}')
print(f'A metade é {moeda_curso.edit(moeda_curso.metade(t))}')
print(f'Caso ela suba {p}% {moeda_curso.edit(moeda_curso.aumentar(t,p))}')
print(f'Caso ela desvalorize {p}% ficaria {moeda_curso.edit(moeda_curso.diminuir(t,p))}')