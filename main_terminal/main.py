from main_terminal.functions import body_of_menu, lines
from main_terminal.classes import Action

option = 0
list1 = []
while option != 7:
    option = 0
    while option not in list1:
        list1 = body_of_menu(35, 'Cadastrar dívida', 'Buscar dívida', 'Todos os devedores', 'Total de dívidas',
                             'Diminuir uma dívida', 'Excluir dados', 'Fechar programa')

        try:
            option = str(input('Digite uma opção: '))
            if option not in list1:
                lines()
                print('ERRO 01: DIGITE UM NÚMERO VÁLIDO!')
        except:
            print('ERROR 02: HOUVE UM ERRO AO ANALISAR SUA OPÇÃO.')
    if option == '7':
        lines()
        print('Fechando o programa...')
        break
    Action(option)
    print('FIM!')
