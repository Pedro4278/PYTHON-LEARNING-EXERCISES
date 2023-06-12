#escreva uma função de uma linha que se adapte ao seu texto

def escrever (texto):
    print('-'* len(texto))
    print(texto)
    print('-'*len(texto))



msg=input('Escreva: ')
escrever(msg)

