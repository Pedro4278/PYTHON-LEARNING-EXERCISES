import PySimpleGUI as sg

sg.theme('Reddit')
layout=[
    [sg.Text('nome'), sg.Input(key='Nome')],
    [ sg.Button('começar')]
]
janela=sg.Window('Teste 01',layout)

print("ASSISTENTE DE MERCADO")
#QUAL TOTAL GASTO NA COMPRA
#QUANTOS PRODUTOS CUSTAM MAIS DO QUE 1000
#QUAL O PRODUTO COM MENOR PREÇO
maisde1000=0
menorpreço=0
cont=0
nomemenor=0
p=0
total=0
comando=0
produtos=[]


while True:

 ação,ler=janela.read()
 if ação == sg.WINDOW_CLOSED:
     break

 if ação == 'começar':
  if ler['Nome'] == 'Pedro':
     print('Autorizado')

  while p != "encerrar":

    if cont > 0:
        p = input('Quando quiser analisar digite "pause", para cadastrar novos produtos digite enter, para finalizar digite "encerrar": ').lower()
        if p == 'encerrar':
            print(f'\033[7;34;40m O produto com menor preço foi o {nomemenor} custando R$ {menorpreço} \033[m')
            print(f'\033[7;34;40m A sua compra tem {maisde1000} produtos que custam R$ 1000,00 ou mais\033[m')
            print(f"\033[7;34;40m O valor total da compra ficou R$ {total} \033[m")

            for produto in produtos:
                print(produto[0], produto[1])
            print('Programa encerrado')

            break

        if p == "pause":
            print(f'\033[7;34;40m O produto com menor preço foi o {nomemenor} custando R$ {menorpreço} \033[m')
            print(f'\033[7;34;40m A sua compra tem {maisde1000} produtos que custam R$ 1000,00 ou mais\033[m')
            print(f"\033[7;34;40m O valor total da compra ficou R$ {total} \033[m")
            comando=input("Digite 'ok' para adicionar mais produtos, 'a' para lista de produtos, 'enter' para encerrar: ")
            if comando == "ok":
                continue

            if comando == 'a':
                for produto in produtos:
                    print(produto[0], produto[1])
                #comando2=input("Deseja cadastrar mais produtos[s/n]?")
               #falta concertar
               # if comando2 == "s":
                  #  continue
               # else:
                   # break

           # else:
               # break


    print(f"Cadastre o {cont}° produto")
    nome=input('Digite o nome do produto: ')
    preço=float(input("Digite o preço: "))


    if cont == 0:
      menorpreço=preço

    if preço <= menorpreço:
        menorpreço=preço
        nomemenor=nome


    if preço >= 1000:
       maisde1000 += 1

    cont += 1
    total += preço
    produtos.append((nome, preço))
