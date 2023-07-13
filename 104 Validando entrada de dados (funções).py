#Crie uma função que leia um input fazendo a validação se é um numero inteiro ou não

def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('ESTE VALOR ESTA INCORRETO, DIGITE UM NUMERO VALIDO')
        if ok:
            break
    return valor


n = leiaint('digite um valor: ')
