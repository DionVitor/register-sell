import PySimpleGUI as sg
from actions import Action

sg.theme('Reddit')
layout = [
    [sg.Text('1 - Cadastrar dívida')],
    [sg.Text('2 - Buscar dívida')],
    [sg.Text('3 - Todos os devedores')],
    [sg.Text('4 - Total de dívidas')],
    [sg.Text('5 - Diminuir uma dívida')],
    [sg.Text('6 - Excluir dados')],
    [sg.Text('7 - Fechar programa')],
    [sg.Text('Digite uma opção:'), sg.Input(key='option', size=(15, 0)), sg.Button('OK'), sg.Button('Sair')]
]

window = sg.Window('Cadastramento de dívidas', layout)
while True:
    eventos, valores = window.read()

    print(eventos)
    print(valores)

    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break
    if valores['option'] not in '1234567':
        sg.popup('Erro!', 'Digite uma opção válida!')
    else:
        Action(valores['option'])