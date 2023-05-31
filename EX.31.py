

print('\033[32m TERMINAL \033[33mINTELIGENTE\033[m')

print('\033[7;4;40m CALCULE AQUI O VALOR DA SUA PASSAGEM: \033[m')

v=int(input("Qual a distancia em kilometros da sua viagem? "))

if v <=200:
    r= v*50
    print('O valor da passagem é R$ {}'.format(r))
else:
    r2= v*45
    print('O valor da sua passagem é R$ {}'.format(r2))
