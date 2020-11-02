from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from functions import append_in_data
from kivy.uix.popup import Popup

layout = GridLayout()


class ScreenMenu(Screen):
    def __init__(self, **kwargs):
        super(ScreenMenu, self).__init__(**kwargs)

        layout_box = BoxLayout()
        layout_box.orientation = 'vertical'
        layout_box.padding = 10

        layout_box.add_widget(Label(text='MENU', font_size=40))
        layout_box.add_widget(Button(text='Cadastrar dívida', on_release=self.change_screen_for_register))
        layout_box.add_widget(Button(text='Buscar dívida'))
        layout_box.add_widget(Button(text='Todos os devedores'))
        layout_box.add_widget(Button(text='Total de dívidas'))
        layout_box.add_widget(Button(text='Diminuir uma dívida'))
        layout_box.add_widget(Button(text='Excluir dados'))

        self.add_widget(layout_box)

    def change_screen_for_register(self, *args):
        self.manager.current = 'register'


class ScreenRegister(Screen):
    def __init__(self, **kwargs):
        super(ScreenRegister, self).__init__(**kwargs)

        global layout

        layout.cols = 2
        layout.padding = 20

        layout.add_widget(Label(text='Comprador:'))
        layout.buyer = TextInput()
        layout.add_widget(layout.buyer)

        layout.add_widget(Label(text='Produto:'))
        layout.product = TextInput()
        layout.add_widget(layout.product)

        layout.add_widget(Label(text='Preço:'))
        layout.price = TextInput()
        layout.add_widget(layout.price)

        layout.add_widget(Label())
        layout.add_widget(Label())

        layout.add_widget(Button(text='VOLTAR', on_release=self.back_to_menu))
        layout.add_widget(Button(text='CONFIRMAR', on_release=self.confirm))

        self.add_widget(layout)

    def back_to_menu(self, *args):
        self.manager.current = 'menu'

    def confirm(self, *args):

        buyer = layout.buyer.text.title()
        product = layout.product.text
        price = layout.price.text

        info = f'{buyer}/{product}/{price}'

        # POPUP
        def exit_popup(*args):
            popup.dismiss()

        def confirm_popup(*args):
            append_in_data('banco_de_dados.txt', info)
            popup.dismiss()
            self.manager.current = 'menu'
            layout.buyer.text = ''
            layout.product.text = ''
            layout.price.text = ''

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


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(ScreenMenu(name='menu'))
sm.add_widget(ScreenRegister(name='register'))


class System(App):
    def build(self):
        return sm


if __name__ == '__main__':
    System().run()
