print('contador masculino e feminino')


n = 1
homem=mulher=0
while n != 'm' and n != 'f':
    n=input('Digite "m" para homem e "f" para mulher: ')
    if n == 'm':
     homem += 1
    elif n == 'f':
        mulher += 1

print('Sucesso! H {} M {}'.format(homem,mulher) )