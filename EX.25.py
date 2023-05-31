
print('DETECTADOR DE SILVAS')

v=input('Digite aqui seu nome ')
f=v.split()
nome=(f[0])

if('silva'in v or 'Silva' in v or 'SILVA' in v):

    print('\033[42m {} você é um membro da Familia Silva! \033[m'.format(nome))
else:
        print('\033[31m {} você não é um membro da famlia Silva \033[m'.format(nome))
        

