
print('DESCUBRA SE O ANO É BISSESTO')

v=int(input('Digite o ano aqui'))
if v % 4 == 0:
    print('O ano {} Este ano é bissesto'.format(v))
else:
    print('O ano {} não é bissesto'.format(v))