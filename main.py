from functions import bobyOfMenu

list1 = bobyOfMenu(35, 'Cadastrar venda', 'Histórico de vendas', 'Relatório de dívidas pendentes')
option = str(input('Digite uma opção: '))

while option not in list1:
    bobyOfMenu(35, 'Cadastrar venda', 'Histórico de vendas', 'Relatório de dívidas pendentes')
    option = str(input('Digite uma opção: '))
