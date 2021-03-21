from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from default_widgets import DefaultTextInput, DefaultButton, DefaultHeadLabel, DefaultLabel, DefaultPopup, \
    DefaultButtonForPopup
from default_layouts import DefaultBoxLayout
from functions import lines_in_archive, append_in_data


Window.size = (360, 640)  # REMOVER
size_screen = Window.size

size_screen_x = 360  # = size_screen[0]
size_screen_y = 640  # = size_screen[1]

payment = 0
file = 'banco_de_dados.txt'

layout_register = DefaultBoxLayout(size_screen)
layout_search = DefaultBoxLayout(size_screen)
layout_total_debts = DefaultBoxLayout(size_screen)
layout_extract = DefaultBoxLayout(size_screen)
layout_all_debtors = DefaultBoxLayout(size_screen)
layout_all_debts = DefaultBoxLayout(size_screen)
layout_payment = DefaultBoxLayout(size_screen)
layout_remove_data = DefaultBoxLayout(size_screen)

scroll_layout_extract = ScrollView()
widget_for_scroll_extract = BoxLayout(orientation='vertical')

scroll_layout_all_debtors = ScrollView()
widget_for_scroll_all_debtors = BoxLayout(orientation='vertical')


class ScreenMenu(Screen):
    def __init__(self, **kwargs):
        super(ScreenMenu, self).__init__(**kwargs)

        layout_menu = DefaultBoxLayout(size_screen)
        layout_menu.spacing = 2.5

        layout_menu.add_widget(DefaultLabel(text='MENU', font_size=size_screen[1] / 15))
        layout_menu.add_widget(Button(text='Cadastrar dívida', on_release=self.change_screen_for_register))
        layout_menu.add_widget(Button(text='Buscar dívida', on_release=self.change_screen_for_search))
        layout_menu.add_widget(Button(text='Todos os devedores', on_release=self.change_screen_for_all_debtors))
        layout_menu.add_widget(Button(text='Total de dívidas', on_release=self.change_screen_for_all_debts))
        layout_menu.add_widget(Button(text='Diminuir uma dívida', on_release=self.change_screen_for_payment))
        layout_menu.add_widget(Button(text='Excluir dados', on_release=self.change_screen_for_remove_data))

        self.add_widget(layout_menu)

    def change_screen_for_register(self, *args):
        self.manager.current = 'register'

    def change_screen_for_search(self, *args):
        self.manager.current = 'search'

    def change_screen_for_all_debtors(self, *args):
        self.manager.current = 'all_debtors'

    def change_screen_for_all_debts(self, *args):
        self.manager.current = 'all_debts'

    def change_screen_for_payment(self, *args):
        self.manager.current = 'payment'

    def change_screen_for_remove_data(self, *args):
        self.manager.current = 'remove_data'

    def back_to_menu(self, window, key, *args):
        if key == 27:
            App.stop()
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)


class ScreenRegister(Screen):
    def __init__(self, **kwargs):
        super(ScreenRegister, self).__init__(**kwargs)

        global layout_register

        layout_register.add_widget(DefaultHeadLabel(size_screen, text='Cadastro'))

        layout_register.buyer = DefaultTextInput(size_screen, hint_text='Comprador')
        layout_register.add_widget(layout_register.buyer)

        layout_register.product = DefaultTextInput(size_screen, hint_text='Produto')
        layout_register.add_widget(layout_register.product)

        layout_register.price = DefaultTextInput(size_screen, hint_text='Preço')
        layout_register.add_widget(layout_register.price)

        layout_register.add_widget(DefaultButton(size_screen, text='CONFIRMAR', on_release=self.confirm))

        layout_register.error = DefaultLabel()
        layout_register.add_widget(layout_register.error)

        self.add_widget(layout_register)

    def back_to_menu(self, window, key, *args):
        if key == 27:
            self.manager.current = 'menu'
            layout_register.error.text = ''
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)

    def confirm(self, *args):
        try:
            valor = layout_register.price.text.replace(',', '.').strip()
            float(valor)
            layout_register.error.text = ''
        except:
            layout_register.error.text = 'Valor digitado inválido!'
            return 0

        buyer = layout_register.buyer.text.title().strip()
        product = layout_register.product.text.strip()
        price = layout_register.price.text.replace(",", ".").strip()

        info = f'{buyer}/{product}/{price}'

        # POPUP
        def exit_popup(*args):
            popup.dismiss()

        def confirm_popup(*args):
            append_in_data(file, info)
            popup.dismiss()
            self.manager.current = 'menu'
            layout_register.buyer.text = ''
            layout_register.product.text = ''
            layout_register.price.text = ''

        content = BoxLayout()
        content.orientation = 'vertical'
        content.add_widget(Label(text=f'Você realmente deseja adicionar:\n'
                                      f'Comprador: {buyer}\n'
                                      f'Produto: {product}\n'
                                      f'Preço: {price}\n',
                                 halign='center'))

        content.add_widget(DefaultButtonForPopup(size_screen, text='Voltar', on_release=exit_popup))

        content.add_widget(DefaultButtonForPopup(size_screen, text='Confirmar', on_release=confirm_popup))

        popup = DefaultPopup(size_screen, title='Confirmação', content=content)

        popup.open()
        # END - POPUP


class ScreenSearch(Screen):
    def __init__(self, **kwargs):
        super(ScreenSearch, self).__init__(**kwargs)

        global layout_search

        layout_search.add_widget(DefaultHeadLabel(size_screen, text='Pesquisar por cliente'))

        layout_search.add_widget(DefaultButton(screen_size=(size_screen_x, size_screen_y * 2), text='Total de dívidas',
                                               on_release=self.change_screen_for_total_debts))
        layout_search.add_widget(DefaultButton(screen_size=(size_screen_x, size_screen_y * 2), text='Extrato de vendas',
                                               on_release=self.change_screen_for_extract))

        layout_search.add_widget(DefaultLabel())
        self.add_widget(layout_search)

    def back_to_menu(self, window, key, *args):
        if key == 27:
            self.manager.current = 'menu'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)

    def change_screen_for_total_debts(self, *args):
        self.manager.current = 'total_debts'

    def change_screen_for_extract(self, *args):
        self.manager.current = 'extract'


class ScreenTotalDebts(Screen):
    def __init__(self, **kwargs):
        super(ScreenTotalDebts, self).__init__(**kwargs)

        global layout_total_debts

        layout_total_debts.add_widget(DefaultHeadLabel(size_screen, text='Total de dívidas'))

        layout_total_debts.search = DefaultTextInput(size_screen, hint_text='Nome do cliente')
        layout_total_debts.add_widget(layout_total_debts.search)

        layout_total_debts.add_widget(DefaultButton(size_screen, text='Procurar', on_release=self.search))

        layout_total_debts.infos = DefaultLabel(halign='center')
        layout_total_debts.add_widget(layout_total_debts.infos)

        self.add_widget(layout_total_debts)

    def back_to_search(self, window, key, *args):
        if key == 27:
            layout_total_debts.search.text = ''
            layout_total_debts.infos.text = ''
            self.manager.current = 'search'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_search)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_search)

    def search(self, *args):
        search = layout_total_debts.search.text.title()
        total_debt = 0
        total_purchase = 0
        exist_client = False

        with open(file) as archive:
            for c in range(0, lines_in_archive(file)):
                line = archive.readline().replace('\n', '').split('/')

                if line[0] == search:
                    total_debt += float(line[2])
                    if line[1] != '**pagamento**':
                        total_purchase += 1
                        exist_client = True
        if exist_client:
            if total_purchase != 1:
                s = 'compras'
            else:
                s = 'compra'
            layout_total_debts.infos.text = f'{total_purchase} {s} do cliente encontada!\n' \
                                            f' Dívida total de {total_debt} reias'
        else:
            layout_total_debts.infos.text = 'Cliente não encontrado!'


class ScreenExtract(Screen):
    def __init__(self, **kwargs):
        super(ScreenExtract, self).__init__(**kwargs)

        global layout_extract
        global scroll_layout_extract
        global widget_for_scroll_extract

        layout_extract.add_widget(DefaultHeadLabel(size_screen, text='Extrato'))

        layout_extract.search = DefaultTextInput(size_screen, hint_text='Nome do cliente')
        layout_extract.add_widget(layout_extract.search)

        layout_extract.add_widget(DefaultButton(size_screen, text='Pesquisar', on_release=self.search_extract))

        layout_extract.label_of_client = DefaultLabel(text='Cliente: ', size_hint=(1, None), height=size_screen[1] / 13)
        layout_extract.add_widget(layout_extract.label_of_client)

        widget_for_scroll_extract.size_hint_y = None
        scroll_layout_extract.add_widget(widget_for_scroll_extract)

        layout_extract.add_widget(scroll_layout_extract)

        layout_extract.total_debts = DefaultLabel(text='Total: R$', size_hint=(1, None), height=size_screen[1] / 13)
        layout_extract.add_widget(layout_extract.total_debts)

        self.add_widget(layout_extract)

    def search_extract(self, *args):
        layout_extract.label_of_client.text = f'Cliente: {layout_extract.search.text.title()}'

        global widget_for_scroll_extract
        widget_for_scroll_extract.clear_widgets()

        with open(file) as archive:
            cont = 0
            total_debts = 0
            list_with_payments = []
            for c in range(0, lines_in_archive(file)):
                line = archive.readline().replace('\n', '').split('/')
                if line[0] == layout_extract.search.text.title():
                    total_debts += float(line[2])
                    if line[1] != '**pagamento**':
                        widget_for_scroll_extract.add_widget(DefaultLabel(text=f'Compra: {line[1]}\nPreço: {line[2]}',
                                                                          size_hint=(1, None),
                                                                          height=size_screen[1] / 10))
                        cont += 1
                    else:
                        list_with_payments.append(f'{line[2]}')

            layout_extract.total_debts.text = f'Total: R${total_debts:.2f}'

            for items in list_with_payments:
                widget_for_scroll_extract.add_widget(DefaultLabel(text=f'PAGAMENTO\nPreço: {items.replace("-", "")}',
                                                                  size_hint=(1, None), height=size_screen[1] / 10))
                cont += 1

        widget_for_scroll_extract.height = (size_screen[1] / 10) * cont

    def back_to_search(self, window, key, *args):
        if key == 27:
            layout_extract.search.text = ''
            widget_for_scroll_extract.clear_widgets()
            layout_extract.label_of_client.text = 'Cliente: '
            layout_extract.total_debts.text = 'Total: R$'
            self.manager.current = 'search'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_search)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_search)


class ScreenAllDebtors(Screen):
    def __init__(self, **kwargs):
        super(ScreenAllDebtors, self).__init__(**kwargs)

        global scroll_layout_all_debtors
        global widget_for_scroll_all_debtors
        global layout_all_debtors

        widget_for_scroll_all_debtors.clear_widgets()
        widget_for_scroll_all_debtors.size_hint_y = None

        layout_all_debtors.add_widget(DefaultHeadLabel(size_screen, text='Todos os devedores'))
        layout_all_debtors.add_widget(DefaultButton(size_screen, text='Pesquisar', on_release=self.search_all_debtors))

        layout_all_debtors.add_widget(scroll_layout_all_debtors)

        self.add_widget(layout_all_debtors)

    def back_to_menu(self, window, key, *args):
        if key == 27:
            widget_for_scroll_all_debtors.clear_widgets()
            self.manager.current = 'menu'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)

    def search_all_debtors(self, *args):
        scroll_layout_all_debtors.clear_widgets()
        widget_for_scroll_all_debtors.clear_widgets()
        list_with_debtors = []
        cont = 0

        with open(file) as archive:
            for c in range(0, lines_in_archive(file)):
                line = archive.readline().replace('\n', '').split('/')

                if line[0] not in list_with_debtors:
                    widget_for_scroll_all_debtors.add_widget(DefaultLabel(text=f'{cont + 1} - {line[0]}',
                                                                          size_hint=(1, None),
                                                                          height=size_screen[1] / 13))
                    cont += 1
                    list_with_debtors.append(line[0])

        if not list_with_debtors:
            widget_for_scroll_all_debtors.add_widget(DefaultLabel(text='Não existe devedores cadastrados!',
                                                                  size_hint=(1, None), height=size_screen[1] / 13))
            cont = 1

        widget_for_scroll_all_debtors.height = (size_screen[1] / 13) * cont
        scroll_layout_all_debtors.add_widget(widget_for_scroll_all_debtors)


class ScreenAllDebts(Screen):
    def __init__(self, **kwargs):
        super(ScreenAllDebts, self).__init__(**kwargs)
        global layout_all_debts

        layout_all_debts.add_widget(DefaultHeadLabel(size_screen, text='Total de dívidas'))
        layout_all_debts.add_widget(DefaultButton(size_screen, text='Pesquisar', on_release=self.search_all_debts))

        layout_all_debts.infos = DefaultLabel(text='O valor total de dívida é:')
        layout_all_debts.add_widget(layout_all_debts.infos)

        self.add_widget(layout_all_debts)

    def back_to_menu(self, window, key, *args):
        if key == 27:
            layout_all_debts.infos.text = 'O valor total da dívida é:'
            self.manager.current = 'menu'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)

    def search_all_debts(self, *args):
        total = 0
        with open(file) as archive:
            for c in range(0, lines_in_archive(file)):
                line = archive.readline().replace('\n', '').split('/')
                total += float(line[2])

        total_real = float(f'{total:.2f}')
        layout_all_debts.infos.text = f'O valor total da dívida é: {total_real}'


class ScreenPayment(Screen):
    def __init__(self, **kwargs):
        super(ScreenPayment, self).__init__(**kwargs)

        global layout_payment

        layout_payment.add_widget(DefaultHeadLabel(size_screen, text='Realizar pagamento'))

        layout_payment.input_name = DefaultTextInput(size_screen, hint_text='Nome do pagante')
        layout_payment.add_widget(layout_payment.input_name)

        layout_payment.input_payment = DefaultTextInput(size_screen, hint_text='Valor do pagamento')
        layout_payment.add_widget(layout_payment.input_payment)

        layout_payment.add_widget(DefaultButton(size_screen, text='Confirmar', on_release=self.confirmation))

        layout_payment.label = DefaultLabel()
        layout_payment.add_widget(layout_payment.label)

        self.add_widget(layout_payment)

    def confirmation(self, *args):
        global payment
        name = layout_payment.input_name.text.title().strip()
        total_debt = 0
        exist_client = False

        with open(file) as archive:
            for c in range(0, lines_in_archive(file)):
                line = archive.readline().replace('\n', '').split('/')
                if line[0] == name:
                    total_debt += float(line[2])
                    exist_client = True

        if not exist_client:
            layout_payment.label.text = f'Não existe um cliente {name} registrado!'

        else:
            total_debt_real = float(f'{total_debt:.2f}')

            if total_debt_real > 0:
                product = '**pagamento**'
                try:
                    payment = float(layout_payment.input_payment.text.replace(',', '.'))
                except:
                    layout_payment.label.text = 'Valor de pagamento inválido!'
                else:
                    if total_debt_real - payment < 0:
                        layout_payment.label.text = f'{name} tem divida de {total_debt_real} reais.\n' \
                                                    f'É impossível reduzir {payment} de {total_debt_real}!'

                    else:
                        # OPEN POP UP
                        def exit_popup(*args):
                            popup.dismiss()

                        def confirm_popup(*args):
                            append_in_data(file, f'{name}/{product}/{payment * -1}')
                            popup.dismiss()
                            self.manager.current = 'menu'
                            layout_payment.input_name.text = ''
                            layout_payment.input_payment.text = ''
                            layout_payment.label.text = ''

                        content = BoxLayout()
                        content.orientation = 'vertical'
                        content.add_widget(Label(text=f'Você realmente deseja quitar a dívida:\n'
                                                      f'Comprador: {name}\n'
                                                      f'Preço: {payment}\n',
                                                 halign='center'))

                        content.add_widget(DefaultButtonForPopup(size_screen, text='Voltar', on_release=exit_popup))

                        content.add_widget(DefaultButtonForPopup(size_screen, text='Confirmar',
                                                                 on_release=confirm_popup))

                        popup = DefaultPopup(size_screen, title='Confirmação', content=content)

                        popup.open()
                        # END POP UP
            else:
                layout_payment.label.text = f'O cliente {name} não possui dívidas.'

    def back_to_menu(self, window, key, *args):
        if key == 27:
            layout_payment.label.text = ''
            self.manager.current = 'menu'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)


class ScreenRemoveData(Screen):
    def __init__(self, **kwargs):
        super(ScreenRemoveData, self).__init__(**kwargs)

        global layout_remove_data

        layout_remove_data.add_widget(DefaultHeadLabel(size_screen, text='Excluir dados'))

        layout_remove_data.name = DefaultTextInput(size_screen, hint_text='Apagar dados de')
        layout_remove_data.add_widget(layout_remove_data.name)

        layout_remove_data.add_widget(DefaultButton(size_screen, text='Excluir dados do usuário',
                                                    on_release=self.delete_data_confirmation))

        layout_remove_data.label = DefaultLabel()
        layout_remove_data.add_widget(layout_remove_data.label)

        layout_remove_data.add_widget(DefaultButton(size_screen, text='Apagar todos os dados',
                                                    on_release=self.delete_all_data_confirmation))

        self.add_widget(layout_remove_data)

    def back_to_menu(self, window, key, *args):
        if key == 27:
            layout_remove_data.label.text = ''
            layout_remove_data.name.text = ''
            self.manager.current = 'menu'
            return True

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.back_to_menu)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.back_to_menu)

    def delete_data_confirmation(self, *args):
        with open(file) as archive:
            global lines
            lines = archive.readlines()

        global list_with_all_debtors
        list_with_all_debtors = []

        for line in lines:
            list_individual = line.replace('\n', '').split('/')
            if list_individual[0] not in list_with_all_debtors:
                list_with_all_debtors.append(list_individual[0])

        if layout_remove_data.name.text.title().strip() not in list_with_all_debtors:
            layout_remove_data.label.text = 'Devedor não encontrado!'
            return 0

        # POP UP
        def exit_popup(*args):
            popup.dismiss()

        def confirm_popup(*args):
            popup.dismiss()
            self.manager.current = 'menu'
            with open(file, 'w') as archive:
                for line in lines:
                    list_ind = line.replace('\n', '').split('/')
                    if list_ind[0] != layout_remove_data.name.text.title().strip():
                        archive.write(f'{list_ind[0]}/{list_ind[1]}/{list_ind[2]}\n')

            layout_remove_data.label.text = ''
            layout_remove_data.name.text = ''

        content = BoxLayout()
        content.orientation = 'vertical'
        content.add_widget(Label(text=f'Você realmente deseja excluir os dados:\n'
                                      f'Devedor: {layout_remove_data.name.text.title().strip()}'))

        btn = Button(text='Voltar', size_hint=(None, None), size=(375, 50), on_release=exit_popup)
        content.add_widget(btn)

        btn2 = Button(text='Confirmar', size_hint=(None, None), size=(375, 50), on_release=confirm_popup)
        content.add_widget(btn2)

        popup = Popup(title='Confirmação',
                      content=content,
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)

        popup.open()
        # END - POPUP

    def delete_all_data_confirmation(self, *args):
        def exit_popup(*args):
            popup.dismiss()

        def confirm_popup(*args):
            popup.dismiss()
            self.manager.current = 'menu'

            with open(file, 'w') as archive:
                archive.write('')

            layout_remove_data.label.text = ''
            layout_remove_data.name.text = ''

        content = BoxLayout()
        content.orientation = 'vertical'
        content.add_widget(Label(text=f'Você realmente deseja excluir TODOS os dados?\n'))

        btn = Button(text='Voltar', size_hint=(None, None), size=(375, 50), on_release=exit_popup)
        content.add_widget(btn)

        btn2 = Button(text='Confirmar', size_hint=(None, None), size=(375, 50), on_release=confirm_popup)
        content.add_widget(btn2)

        popup = Popup(title='Confirmação',
                      content=content,
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)

        popup.open()


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.transition = FadeTransition()
        self.add_widget(ScreenMenu(name='menu'))
        self.add_widget(ScreenRegister(name='register'))
        self.add_widget(ScreenSearch(name='search'))
        self.add_widget(ScreenTotalDebts(name='total_debts'))
        self.add_widget(ScreenExtract(name='extract'))
        self.add_widget(ScreenAllDebtors(name='all_debtors'))
        self.add_widget(ScreenAllDebts(name='all_debts'))
        self.add_widget(ScreenPayment(name='payment'))
        self.add_widget(ScreenRemoveData(name='remove_data'))


class System(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    System().run()
