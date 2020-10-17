from functions import body_of_menu, lines
from classes import Action

option = 0
list1 = []

while option not in list1:
    list1 = body_of_menu(35, 'Cadastrar venda', 'Buscar vendas', 'Relatório de dívidas pendentes',
                         'Excluir dívida/venda', 'Diminuir uma dívida')

    try:
        option = str(input('Digite uma opção: '))
        if option not in list1:
            lines()
            print('ERRO 01: DIGITE UM NÚMERO VÁLIDO!')
    except:
        print('ERROR 02: HOUVE UM ERRO AO ANALISAR SUA OPÇÃO.')

Action(option)
