from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class DefaultTextInput(TextInput):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultTextInput, self).__init__(**kwargs)
        
        self.font_size = screen_size[1] / 35
        self.size_hint = (1, None)
        self.height = screen_size[1] / 15
        self.multiline = False


class DefaultButton(Button):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultButton, self).__init__(**kwargs)

        self.size_hint = (1, None)
        self.height = screen_size[1] / 15


class DefaultHeadLabel(Label):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultHeadLabel, self).__init__(**kwargs)

        self.font_size = screen_size[1] / 25
        self.size_hint = (1, None)
        self.height = screen_size[1] / 5
        self.color = (0, 0, 0, 1)

        self.text_size = (screen_size[0] - 20, None)
        self.halign = 'left'
