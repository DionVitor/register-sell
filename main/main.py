from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class ScreenMenu(Screen):
    def __init__(self, **kwargs):
        super(ScreenMenu, self).__init__(**kwargs)

        layout = BoxLayout()
        layout.orientation = 'vertical'

        layout.add_widget(Label(text='MENU', font_size=40))
        layout.add_widget(Button(text='Cadastrar dívida', on_release=self.change_screen_for_register))
        layout.add_widget(Button(text='Buscar dívida'))
        layout.add_widget(Button(text='Todos os devedores'))
        layout.add_widget(Button(text='Total de dívidas'))
        layout.add_widget(Button(text='Diminuir uma dívida'))
        layout.add_widget(Button(text='Excluir dados'))

        self.add_widget(layout)

    def change_screen_for_register(self, *args):
        self.manager.current = 'register'


class ScreenRegister(Screen):
    def __init__(self, **kwargs):
        super(ScreenRegister, self).__init__(**kwargs)

        layout = GridLayout()

        layout.cols = 2
        layout.padding = 40

        layout.add_widget(Label(text='Comprador:'))
        layout.add_widget(TextInput())

        layout.add_widget(Label(text='Produto:'))
        layout.add_widget(TextInput())

        layout.add_widget(Label(text='Preço:'))
        layout.add_widget(TextInput())

        layout.add_widget(Label())
        layout.add_widget(Label())

        layout.add_widget(Button(text='VOLTAR', on_release=self.back_to_menu))
        layout.add_widget(Button(text='CONFIRMAR'))

        self.add_widget(layout)

    def back_to_menu(self, *args):
        self.manager.current = 'menu'


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(ScreenMenu(name='menu'))
sm.add_widget(ScreenRegister(name='register'))


class System(App):
    def build(self):
        return sm


if __name__ == '__main__':
    System().run()
