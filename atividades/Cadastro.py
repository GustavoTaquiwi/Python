from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkAmber')  # Corrigido o tema
layout = [
    [sg.Text('Gustavo Taquiwi Ariosi')],
    [sg.Text('Envie Sua Mensagem?'), sg.Input(key='algo')],
    [sg.Button('Enviar')],
]
#Layout 2
layout2 = [
[sg.Text('Mensagem Encaminhada!!')],
[sg.Text('', size=(30, 1), key='-ALGO_RESULT-')],]

# Janela
janela = sg.Window('Tela de Login', layout)

#Janela 2

janela2 = sg.Window ('Desafio Proposto!',layout2 , finalize=True)
janela2.hide()

# Ler os Eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Enviar':
       algo = valores['algo'] 
       
       janela.hide()
       janela2['-ALGO_RESULT-'].update(f'"{algo}"')
       janela2.un_hide()

evento2, _ = janela2.read()
janela2.close()
janela.close()
