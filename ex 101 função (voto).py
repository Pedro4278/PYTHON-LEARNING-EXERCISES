import datetime

#Crie uma função que recebe o ano de nascimento e responde se
#O voto é opcional, obrigatorio ou negado


def voto(ano):
    data_atual= datetime.datetime.now()
    ano_atual= data_atual.year
    idade= ano_atual - ano

    if idade >= 18 and idade <= 64:
        print(f'Com {idade} anos o voto é obrigatorio')
    if idade < 16:
        print(f'Com {idade} anos você ainda não pode votar')
    if idade < 18 and idade > 16:
        print(f'Com {idade} anos o voto é opcional')
    if idade >= 65:
        print(f'Com {idade} anos o voto é opcional')



voto(1980)

