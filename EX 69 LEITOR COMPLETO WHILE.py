maiores=0
homens=0
mulher20=0
cont=0
per=0
while per != 'pare':

    if cont != 0:
        per=input('Quando quiser encerrar o cadastro digite \033[30;41m"pare"\033[m caso contrario aperte \033[30;42m "ENTER":\033[m ').lower()

    if per == 'pare':
        print(f'\033[7;30;44m São {maiores} pessoas maiores de 18 anos \033[m')
        if homens > 1:
         print(f'\033[7;30;44m{homens} homens\033[m')
        if homens == 0:
            print('\033[7;30;44mVocê não cadastrou nenhum homem\033[m')
        if homens == 1:
            print('\033[7;30;44mSomente 1 homem foi cadastrado\033[m')
#FALTA TERMINAR AQUI!!!!!!!!!
        print(f'\033[7;30;44m{mulher20} Mulheres menores de 20 anos\033[m')
        break
    cont += 1

    print(f'\033[7;30;44m---- {cont}° PESSOA ---- \033[m')
    nome=input('Digite o nome: ').lower()
    sexo=input('Digite H para homem e M para mulher: ').lower()
    idade=int(input('Digite a idade: '))

    if idade > 18:
        maiores += 1
    if sexo == 'h':
        homens += 1
    if sexo == 'm' and idade < 20:
        mulher20 += 1



