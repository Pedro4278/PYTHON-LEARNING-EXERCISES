def aumentar(valor, percentual, format=False):
    aumento = valor * (percentual / 100)
    novo_valor = valor + aumento
    return novo_valor if format is False else edit(valor)


def diminuir(valor, percentual, format=False):
    aumento = valor * (percentual / 100)
    novo_valor = valor - aumento
    return novo_valor if format is False else edit(valor)



def dobro (valor, format=False):
    dobro= valor * 2
    return dobro if format is False else edit(valor)


def metade (valor, format=False):
    metade = valor / 2
    return metade if format is False else edit(valor)

def edit (preço=0, moeda='R$'):
    return f'{moeda} {preço}'.replace('.',',')

def resumo (preço=0, porcetmais=10, porcentmenos=10):
    print('-'*30)
    print('RESUMO DAS PROJEÇÕES'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{edit(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'Com taxa de aumento de {porcetmais}%, ficaria {aumentar(preço,porcetmais,True)}')
    print(f'Com diminuição de {porcentmenos}% ficaria {diminuir(preço,porcentmenos,True)}')
    print('-'*30)

