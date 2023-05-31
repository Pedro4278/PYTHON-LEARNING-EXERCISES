alunos={}
while True:
    alunos['nome:']=input('Digite o nome: ')
    alunos['nota:']=int(input('Digite a nota: '))

    if alunos['nota:'] < 7:
        alunos['situação:']='reprovado'
        print(alunos)
        break
    elif alunos['nota:'] > 7 and alunos['nota:'] <= 10:
        alunos['situação:']='aprovado'
        print (alunos)
        break
    elif alunos ['nota:'] > 10:
        print('Media invalida, digite novamente')


