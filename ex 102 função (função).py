#crie uma função de fatorial que mostre o resultado e todas as contas que foram feitas
#caso sejam solicitadas


def fatorial(numero=0, mostre=False):

    f=1
    for c in range(numero,0,-1):
         if mostre:
             print(f'{f} vezes {c} é igual á')
         f *= c
    else:
     return f



t=fatorial(5, True)
print(t)
