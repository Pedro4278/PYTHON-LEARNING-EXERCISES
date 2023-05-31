print('Tabela do Brasileirão')

while True:
    times=('Botafogo\n','Palmeiras\n','Cruzeiro\n','Fortaleza\n','São Paulo\n','Fluminense\n','Grêmio\n','Inter\n','Bahia\n','Athletico-PR\n','Vasco\n','Red Bull Bragantino\n','Cuiabá\n','Santos\n','Corinthians\n','Atlético-MG\n','Flamengo\n','Goiás\n','Coritiba\n','América-MG')
    print(times)
    primeiros=(times[0:5])
    ultimos=(times[16:])
    org=sorted(times)
    posi=input('Digite do nome do seu time para saber em que posição ele esta: ')
    result= (times.index(posi))
    resultado=(result+1)

    print(f'O seu time esta a {resultado}° posição, {primeiros} são os primeiros e {ultimos} são os ultimos')
    tabela=input('Digite "t" para vizualizar a tabela completa: ')
    if tabela == 't':
        print(times)
        ter=input('Para organizar o time em ordem alfabetica digite "sim" para encerrar digite "fim": ')
        if ter == 'sim':
            print(org)
        elif ter == 'fim':
            break
