from functions import lines, append_in_data, body_of_menu, lines_in_archive

archive = 'banco_de_dados.txt'
class Action:
    def __init__(self, option):
        if option == '1':
            lines()

            nome = str(input('Digite o nome do comprador: '))
            produto = str(input('Digite qual produto você vendeu: '))
            valor = input('Digite o preço da venda: ')

            try:
                float(valor)
            except:
                print('ERRO 3: O VALOR DA VENDA ESTÁ INCORRETO.')

                valor2 = ''
                while not valor2.isdigit():
                    valor = input('Digite o preço da venda: ')
                    valor2 = valor.replace('.', '0')
                float(valor)
            finally:
                # CRIAR CONFIRMAÇÃO PARA INSERIR OS ARQUIVOS!
                append_in_data(archive, f'{nome.title()}/{produto}/{valor}')
            lines()

        if option == '2':
            list_of_option2 = body_of_menu(35, 'Pesquisar por cliente', 'Ver todas as vendas')
            option2 = 0
            while option2 not in list_of_option2:
                option2 = str(input('Digite uma opção: '))

            if option2 == '1':
                search = str(input('Digite o nome do cliente: ')).title()
                cont = 0
                a = open(archive)
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')

                    if line[0] == search:
                        lines()
                        print(f'Compra do cliente {line[0]} encontrada!\nCompra: {line[1]}\nPreço: {line[2]}')
                        lines()
                a.close()

            if option2 == '2':
                a = open(archive)
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')
                    lines()
                    print(f'Cliente: {line[0]}\nCompra: {line[1]}\nPreço: {line[2]}')
                    lines()
                a.close()
