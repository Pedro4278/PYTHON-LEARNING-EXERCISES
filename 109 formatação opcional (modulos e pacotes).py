#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moeda_curso

t = int(input('Digite o valor da moeda: '))
p= int(input('Digite a porcentagem: '))

print(f'O dobro da moeda é {moeda_curso.edit(moeda_curso.dobro(t, True))}')
print(f'A metade é {moeda_curso.edit(moeda_curso.metade(t, True))}')
print(f'Caso ela suba {p}% {(moeda_curso.aumentar(t,p, True))}')
print(f'Caso ela desvalorize {p}% ficaria {moeda_curso.edit(moeda_curso.diminuir(t,p, True))}')