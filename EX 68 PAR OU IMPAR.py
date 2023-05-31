import random
import time

derrotas=0
vitorias=0
cont=0
print("JOGO DE PAR OU IMPAR PARA SOLITARIOS")


while cont < 6 :

    cont += 1
    op=input('Você quer PAR ou IMPAR? [P/I]: '.lower())
    palp=int(input("Digite o numero entre 0 e 10: "))
    resp=random.randint(1,10)
    tot= resp+palp
    if palp > 10 or palp < 0:
        print('\033[30;41m NUMERO INVALIDO !! \033[m')


#RESULTADO PAR:
    if tot % 2 == 0 and op == 'p':
        print(f'Você jogou {palp} eu  joguei {resp}, {tot} é par então \033[30;32m VOCÊ VENCEU!\033[m')
        vitorias += 1

    if tot % 2 == 0 and op == 'i':
        print(f'Você jogou {palp} eu  joguei {resp}, {tot} é par então  \033[7;30;32m EU VENCI!\033[m')
        derrotas += 1

#RESULTADO IMPAR:
    if tot % 2 != 0 and op == 'i':
        print(f'Você jogou {palp} eu  joguei {resp}, {tot} é impar então  \033[30;32m VOCÊ VENCEU!\033[m')
        vitorias += 1

    if tot % 2 != 0 and op == 'p':
        print(f'Você jogou {palp} eu  joguei {resp}, {tot} é impar então  \033[7;30;32m EU VENCI!\033[m')
        derrotas += 1

print(f'Você venceu {vitorias}\n Eu venci {derrotas}')
if vitorias > derrotas:
    print ('Você é o grande campeão !!!')
if derrotas > vitorias:
    print ('Eu te venci!!!!')