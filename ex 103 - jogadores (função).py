#crie um programa que receba dois parametros, nome e numero de gols
#O programa deve mostrar a ficha do jogador mesmo que algum dado não tenha sido inserido



def format (nome='', gols=0):
    if nome.strip()=='':
        nome = 'desconhecido'
    return f'O jogador {nome} fez {gols} gols'


v=input('Digite o nome do jogador: ')
gols=int(input('Digite o numero de gols: '))

print(format(v,gols))