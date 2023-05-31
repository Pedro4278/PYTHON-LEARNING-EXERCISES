v=int(input('Digite aqui a velocidade '))
if v <=80:
    print('Velocidade dentro do limite')
else:
    r=(v-80)*7
    print ('Você foi multado pague R${},00 ao estado'.format(r))