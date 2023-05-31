from PySimpleGUI import PySimpleGUI as rend

acesso=0
cadeado=0
while cadeado != 2:

    print('Caixa eletronico multiverso')

    rend.theme('Reddit')
    layout= [
        [rend.Text('Digite a sua senha:'), rend.Input(key='senha')],
        [rend.Button('entrar')]
    ]
    janela=(rend.Window('CAIXA ELETRONICO INTERDIMENSIONAL',layout))

    while acesso != 1:
     ação,ler = janela.Read()
     if ação == rend.WINDOW_CLOSED:
          break
     if ação == 'entrar':
         if ler ['senha'] == '2345':
             print('Acesso Autorizado')
             acesso=1

         else:
             [rend.Text('Acesso Negado')]



    v=0
    notas50=0
    notas20=0
    notas5=0
    notas1=0

    #num(50,20,5,1) == ao numero de notas sacadas

    if acesso == 1:
        rend.theme('Reddit')
        layout2=[
            [rend.Text('Bem Vindo Novamente!')],
            [rend.Text('Digite o valor que deseja sacar: ', rend.Input(key='valor'))],
            [rend.Button('sacar')]
        ]
        janela2=(rend.Window('CAIXA ELETRONICO INTERDIMENSIONAL',layout2))


        ler2, ação2 = janela2.read()

    #if acesso ==1:

        if ação2 == rend.WINDOW_CLOSED:
            break


        if ler2.get('valor')>0:
            v.append(ler2.get('valor'))

            num50 = v // 50
            rest50 = v % 50
            if num50 >= 1:
             notas50 += num50
            if rest50 == 0:
                print(f'Você recebera {notas50} notas de R$ 50,00')

            else:
                num20 = rest50 // 20
                rest20 = rest50 % 20
                if num20 >=1:
                    notas20+=num20
                if rest20 == 0:
                    print(f"você receberá {notas50} notas de R$ 50,00 e {notas20} notas de R$20,00")
                elif rest20 != 0 :
                    num5 = rest20 // 5
                    rest5= rest20 % 5
                    if num5 >= 1:
                        notas5+=num5
                    if rest5 == 0:
                        print(f"Você receberá {notas50} notas de R$ 50,00, {notas20} notas de R$ 20,00 e {notas5} notas de R$ 5,00")
                    else:
                        num1 = rest5 * 1
                        notas1 += num1
                        print(f'Você receberá {notas50} notas de R$ 50,00, {notas20} notas de R$ 20,00, {notas5} notas de R$ 5,00 e {notas1} notas de R$ 1,00')
                        print("Obrigado volte sempre!")
                        break
print(f'Você receberá {notas50} notas de R$ 50,00, {notas20} notas de R$ 20,00, {notas5} notas de R$ 5,00 e {notas1} notas de R$ 1,00')
cadeado=2