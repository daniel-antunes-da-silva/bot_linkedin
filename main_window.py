import PySimpleGUI as sg
from janelas import janela_conexao

sg.theme('BluePurple')

# Defina o layout da janela principal
layout = [
    [sg.Text('Escolha a automação:')],
    [sg.Button('Automação de conexões')],
    [sg.Text('')],
    [sg.Button('Automação de publicação')],
    [sg.Button('Sair')]
]

# Defina o tamanho da janela principal
window_size = (400, 200)

# Crie a janela principal
window = sg.Window('Escolha', layout, size=window_size)

# Loop principal
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Automação de conexões':
        janela_conexao()
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
        window2.close()

# Feche a janela principal ao sair do loop
window.close()
