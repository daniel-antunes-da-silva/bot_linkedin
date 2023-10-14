import PySimpleGUI as sg
from threading import Thread
from bot_conexoes import bot_conexoes

sg.theme('Reddit')

layout = [
    [sg.Text('Profissão a buscar'),sg.Input(key='profissao',size=(30,0))],
    [sg.Text('Mensagem a enviar no convite')],
    [sg.Multiline(size=(43, 7),key='mensagem')],
    [sg.Text('Histórico')],
    # Esse aqui exibe os prints no histórico.
    [sg.Output(size=(43, 7))],
    [sg.Button('Enviar',key='botao_enviar')],
]

window = sg.Window('Bot LinkedIn',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'botao_enviar':
        profissao = values['profissao']
        mensagem = values['mensagem']

        thread_bot_linkedin = Thread(target=bot_conexoes,args=(profissao, mensagem), daemon=True)
        thread_bot_linkedin.start()

        window['profissao'].update(disabled=True)
        window['mensagem'].update(disabled=True)
        window['botao_enviar'].update(disabled=True)

