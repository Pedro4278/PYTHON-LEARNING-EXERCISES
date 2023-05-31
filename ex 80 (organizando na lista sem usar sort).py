lista=[]
for c in range(6):
    n=int(input('Digite o valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos=0
        while pos < len(lista):
            if n <=lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1
print('=-'*30)
print(f'Adicionados foram organizados em ordem crescente sem o uso do metodo sort()\n Os numeros são: {lista}')
print('-='*30)