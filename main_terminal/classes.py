from main_terminal.functions import lines, append_in_data, body_of_menu, lines_in_archive

archive = 'database.txt'
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
                lines()
                confirmation = str(input(f'Você realmente deseja adicionar:\nCliente: {nome.title()}\nProduto: {produto}\nValor: {valor}\n[S/N]'))
                lines()
                if confirmation in 'Ss':
                    append_in_data(archive, f'{nome.title()}/{produto}/{valor}')
                    print(f'OK, foi adicionado.')
                else:
                    print(f'OK, não foi adicionado.')
            lines()


        if option == '2':
            list_of_option2 = body_of_menu(35, 'Total de dívida por cliente', 'Extrato de vendas por cliente')
            option2 = 0
            while option2 not in list_of_option2:
                option2 = str(input('Digite uma opção: '))

            if option2 == '1':
                search = str(input('Digite o nome do cliente: ')).title()
                total_debt = 0
                total_purchase = 0
                exist_client = False
                a = open(archive)
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')

                    if line[0] == search:
                        total_debt += float(line[2])
                        if line[1] != '**pagamento**':
                            total_purchase += 1
                            exist_client = True
                a.close()
                lines()
                if exist_client:
                    if total_purchase != 1:
                        s = 'compras'
                    else:
                        s = 'compra'
                    print(f'{total_purchase} {s} do cliente encontrada!\nDívida total de {total_debt} reais.')
                    lines()
                else:
                    print('Cliente não encontrado!')
                    lines()


            if option2 == '2':
                a = open(archive)
                search = str(input('Digite o nome do cliente: ')).title()
                lines()
                cont = 0
                print(f'Cliente {search}:')
                lines()
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')
                    if line[0] == search:
                        if line[1] != '**pagamento**':
                            print(f'Compra: {line[1]}\nPreço: {line[2]}')
                            lines()
                            cont += 1
                if cont == 0:
                    print('Não encontrado!')
                    lines()
                a.close()

                a = open(archive)
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')
                    if line[0] == search:
                        if line[1] == '**pagamento**':
                            print(f'PAGAMENTO: {line[2]}')
                            lines()
                a.close()

                a = open(archive)
                total_debt = 0
                for c in range(0, lines_in_archive(archive)):
                    line = a.readline().replace('\n', '').split('/')
                    if line[0] == search:
                        total_debt += float(line[2])
                print(f'Total da dívida de {search}: {total_debt}')
                lines()


        if option == '3':
            lines()
            list_with_all_debtors = []
            a = open(archive)
            index = 1
            exist_debtor = False
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                if line[0] not in list_with_all_debtors:
                    print(f'{index} - {line[0]}')
                    list_with_all_debtors.append(line[0])
                    index += 1
                    exist_debtor = True
            if exist_debtor:
                lines()
            else:
                print('Ainda não existe devedores.')
                lines()

        if option == '4':
            total = 0
            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                total += float(line[2])
            a.close()
            print(f'O valor total de dívidas é: {total}')
            lines()


        if option == '5':

            nome = ''
            list_with_all_clients = []
            a = open(archive)
            total_debt = 0

            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                list_with_all_clients.append(f'{line[0]}')
            while nome not in list_with_all_clients:
                lines()
                nome = str(input('Digite o nome do pagante: ')).title()
            a.close()

            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                if line[0] == nome:
                    total_debt += float(line[2])
            a.close()

            if total_debt > 0:
                produto = '**pagamento**'
                valor = input('Digite o preço do pagamento: ')
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
                    if total_debt - float(valor) < 0:
                        lines()
                        print(f'{nome} tem dívida de {total_debt} reias.')
                        print(f'É impossível reduzir {valor} de {total_debt}!')
                        lines()

                    else:
                        confirmation = str(input(f'Você realmente deseja quitar essa dívida:\nPagante: {nome.title()}'
                                                 f'\nValor: {valor}\n[S/N]'))
                        lines()
                        if confirmation in 'Ss':
                            append_in_data(archive, f'{nome.title()}/{produto}/{float(valor) * -1}')
                            print(f'OK, foi quitado a dívida de {valor} reias.')
                        else:
                            print(f'OK, não foi quitado a dívida.')
                        lines()

            else:
                print(f'Cliente {nome} não possui dívidas.')
                lines()


        if option == '6':
            list_of_clients = []
            lines()
            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                if line[0] not in list_of_clients:
                    print(f'Cliente: {line[0]}')
                    list_of_clients.append(line[0])
                    lines()
            a.close()

            remove = str(input('Qual cliente você deseja excluir os dados?')).title()
            debt = 0
            exist_client = False
            list_with_outhers_clients = []
            a = open(archive)
            for c in range(0, lines_in_archive(archive)):
                line = a.readline().replace('\n', '').split('/')
                if line[0] == remove:
                    debt += float(line[2])
                    exist_client = True
                else:
                    list_with_outhers_clients.append(line)

            if exist_client:
                print(f'A dívida atual do cliente {remove} é: {debt}')
            else:
                print(f'Cliente {remove} não encontrado.')
            a.close()
            confirmation_remove_debt = str(input(f'Você realmente deseja excluir os dados do cliente {remove}? [S/N]'))
            if confirmation_remove_debt in 'Ss':
                a = open(archive, 'w')
                for c in range(0, len(list_with_outhers_clients)):
                    a.write(f'{list_with_outhers_clients[c][0]}/{list_with_outhers_clients[c][1]}/{list_with_outhers_clients[c][2]}\n')
                a.close()
                print(f'Foi exluído os dados de {remove}.')
            else:
                print(f'Não foi excluído os dados de {remove}.')
