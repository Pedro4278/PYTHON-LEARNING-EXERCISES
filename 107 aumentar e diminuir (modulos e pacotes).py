#crie um modulo com a função aumentar, diminuir dobrar e reduzir pela metade.
# Importe o modulo e aplique no exercicio
import moeda_curso

t = int(input('Digite o valor da moeda: '))

print(f'O dobro da moeda é {moeda_curso.dobro(t)}')
print(f'A metade é {moeda_curso.metade(t)}')
print(f'Caso ela suba 10% {moeda_curso.aumentar(t,10)}')
print(f'Caso ela desvalorize 10% ficaria {moeda_curso.diminuir(t,10)}')


