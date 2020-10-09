from functions import body_of_menu

option = 0
list1 = []

while option not in list1:
    list1 = body_of_menu(35, 'Cadastrar venda', 'Histórico de vendas', 'Relatório de dívidas pendentes')

    try:
        option = str(input('Digite uma opção: '))
        if option not in list1:
            print('-' * 35)
            print('ERRO 01: DIGITE UM NÚMERO VÁLIDO!')
    except:
        print('ERROR 02: HOUVE UM ERRO AO ANALISAR SUA OPÇÃO.')
