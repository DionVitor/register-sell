from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from functions import append_in_data, lines_in_archive
from kivy.uix.popup import Popup

layout_register = GridLayout()
layout_search = BoxLayout()
layout_total_debts = BoxLayout()
file = 'banco_de_dados.txt'


class ScreenMenu(Screen):
    def __init__(self, **kwargs):
        super(ScreenMenu, self).__init__(**kwargs)

        layout_menu = BoxLayout()
        layout_menu.orientation = 'vertical'
        layout_menu.padding = 10

        layout_menu.add_widget(Label(text='MENU', font_size=40))
        layout_menu.add_widget(Button(text='Cadastrar dívida', on_release=self.change_screen_for_register))
        layout_menu.add_widget(Button(text='Buscar dívida', on_release=self.change_screen_for_search))
        layout_menu.add_widget(Button(text='Todos os devedores'))
        layout_menu.add_widget(Button(text='Total de dívidas'))
        layout_menu.add_widget(Button(text='Diminuir uma dívida'))
        layout_menu.add_widget(Button(text='Excluir dados'))

        self.add_widget(layout_menu)

    def change_screen_for_register(self, *args):
        self.manager.current = 'register'

    def change_screen_for_search(self, *args):
        self.manager.current = 'search'


class ScreenRegister(Screen):
    def __init__(self, **kwargs):
        super(ScreenRegister, self).__init__(**kwargs)

        global layout_register

        layout_register.cols = 2
        layout_register.padding = 10

        layout_register.add_widget(Label(text='Comprador:'))
        layout_register.buyer = TextInput()
        layout_register.add_widget(layout_register.buyer)

        layout_register.add_widget(Label(text='Produto:'))
        layout_register.product = TextInput()
        layout_register.add_widget(layout_register.product)

        layout_register.add_widget(Label(text='Preço:'))
        layout_register.price = TextInput()
        layout_register.add_widget(layout_register.price)

        layout_register.add_widget(Label())
        layout_register.add_widget(Label())

        layout_register.add_widget(Button(text='VOLTAR', on_release=self.back_to_menu))
        layout_register.add_widget(Button(text='CONFIRMAR', on_release=self.confirm))

        self.add_widget(layout_register)

    def back_to_menu(self, *args):
        self.manager.current = 'menu'

    def confirm(self, *args):

        buyer = layout_register.buyer.text.title()
        product = layout_register.product.text
        price = layout_register.price.text.replace(",", ".")

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
                                      f'Preço: {price}\n'))

        btn = Button(text='Voltar', size_hint=(None, None), size=(375, 50), on_release=exit_popup)
        content.add_widget(btn)

        btn2 = Button(text='Confirmar', size_hint=(None, None), size=(375, 50), on_release=confirm_popup)
        content.add_widget(btn2)

        popup = Popup(title='Confirmação',
                      content=content,
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)

        popup.open()
        # END - POPUP


class ScreenSearch(Screen):
    def __init__(self, **kwargs):
        super(ScreenSearch, self).__init__(**kwargs)

        global layout_search

        layout_search.orientation = 'vertical'
        layout_search.padding = 10

        layout_search.add_widget(Label(text='Pesquisar por cliente', font_size=25, size_hint=(1, None), height=50))
        layout_search.add_widget(Label(size_hint=(1, None), height=110))
        layout_search.add_widget(Button(text='Total de dívidas', size_hint=(1, None), height=100,
                                        on_release=self.change_screen_for_total_debts))
        layout_search.add_widget(Button(text='Extrato de vendas', size_hint=(1, None), height=100))
        layout_search.add_widget(Label())
        layout_search.add_widget(Button(text='Voltar', size_hint=(1, None), height=50, on_release=self.back_to_menu))
        self.add_widget(layout_search)

    def back_to_menu(self, *args):
        self.manager.current = 'menu'

    def change_screen_for_total_debts(self, *args):
        self.manager.current = 'total_debts'


class ScreenTotalDebts(Screen):
    def __init__(self, **kwargs):
        super(ScreenTotalDebts, self).__init__(**kwargs)

        global layout_total_debts
        layout_total_debts.orientation = 'vertical'
        layout_total_debts.padding = 10

        layout_total_debts.add_widget(Label(text='Nome do cliente:', size_hint=(1, None), height=100, font_size=20))

        layout_total_debts.search = TextInput(multiline=False, size_hint=(1, None), height=50)
        layout_total_debts.add_widget(layout_total_debts.search)

        layout_total_debts.add_widget(Button(text='Procurar', size_hint=(1, None), height=50,
                                             on_release=self.search))

        layout_total_debts.infos = Label(text='0 compras do cliente\nTotal de dívidas: ')
        layout_total_debts.add_widget(layout_total_debts.infos)

        layout_total_debts.add_widget(Button(text='Voltar', size_hint=(1, None), height=50,
                                             on_release=self.back_to_search))

        self.add_widget(layout_total_debts)

    def back_to_search(self, *args):
        self.manager.current = 'search'

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
                s = 'compras'
            layout_total_debts.infos.text = f'{total_purchase} {s} do cliente encontada!\n' \
                                            f' Dívida total de {total_debt} reias'
        else:
            layout_total_debts.infos.text = 'Cliente não encontrado!'


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(ScreenMenu(name='menu'))
sm.add_widget(ScreenRegister(name='register'))
sm.add_widget(ScreenSearch(name='search'))
sm.add_widget(ScreenTotalDebts(name='total_debts'))


class System(App):
    def build(self):
        return sm


if __name__ == '__main__':
    System().run()
