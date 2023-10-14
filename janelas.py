def janela_principal():
    import PySimpleGUI as sg

    sg.theme('Reddit')

    layout = [
        [sg.Text('Bem vindo(a) à janela principal!', text_color='black', font='helvetica 12')],
       # [sg.Text('')],
        [sg.Text('Escolha a automação:', text_color='black', font='helvetica 10')],
        [sg.Text()],
        [sg.Button('Automação de conexões'), sg.Button('Automação de publicação')],
        [sg.Text('')],
        [sg.Button('Sair', size=10)]
    ]

    window_size = (400, 200)

    window = sg.Window('Escolha', layout, size=window_size)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        if event == 'Automação de conexões':
            window.close()
            janela_conexao()
        '''
        if event == 'Abrir Janela 2':
            # Defina o layout da Janela 2
            layout2 = [
                [sg.Text('Janela 2')],
                [sg.Button('Fechar Janela 2')]
            ]
            # Defina o tamanho da Janela 2
            window_size2 = (350, 180)
            # Crie a Janela 2
            window2 = sg.Window('Janela 2', layout2, size=window_size2)
            # Loop da Janela 2
            while True:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED or event2 == 'Fechar Janela 2':
                    break
            window2.close()'''

    window.close()


def janela_conexao():
    import PySimpleGUI as sg
    from threading import Thread
    from bot_conexoes import bot_conexoes
    sg.theme('Reddit')

    layout = [
        [sg.Text('Profissão a buscar'), sg.Input(key='profissao',size=(30, 0))],
        [sg.Text('Mensagem a enviar no convite')],
        [sg.Multiline(size=(43, 7), key='mensagem')],
        [sg.Text('Histórico')],
        # Esse aqui exibe os prints no histórico.
        [sg.Output(size=(43, 7))],
        [sg.Button('Iniciar', key='botao_iniciar', size=(20, 1)),
         sg.Button('Voltar', key='botao_voltar', size=(20, 1))]

    ]

    window = sg.Window('Bot LinkedIn', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'botao_voltar':
            window.close()
            janela_principal()
        elif event == 'botao_iniciar':

            profissao = values['profissao']
            mensagem = values['mensagem']

            thread_bot_linkedin = Thread(target=bot_conexoes, args=(profissao, mensagem), daemon=True)
            thread_bot_linkedin.start()
            if event == sg.WIN_CLOSED:
                window.close()
                break

            window['profissao'].update(disabled=True)
            window['mensagem'].update(disabled=True)
            window['botao_iniciar'].update(disabled=True)


if __name__ == '__main__':
    janela_principal()
