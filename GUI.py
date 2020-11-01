from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyMenuLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyMenuLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='MENU', font_size=40))

        self.add_widget(Button(text='Cadastrar dívida'))

        self.add_widget(Button(text='Buscar dívida'))

        self.add_widget(Button(text='Todos os devedores'))

        self.add_widget(Button(text='Total de dívidas'))

        self.add_widget(Button(text='Diminuir uma dívida'))

        self.add_widget(Button(text='Excluir dados'))


class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 2
        self.padding = 10

        self.add_widget(MyMenuLayout(size_hint=(0.4, 1)))
        self.add_widget(Label())


class System(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    System().run()
