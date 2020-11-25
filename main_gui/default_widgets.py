from kivy.uix.textinput import TextInput


class DefaultTextInput(TextInput):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultTextInput, self).__init__(**kwargs)
        
        self.font_size = screen_size[1] / 35
        self.size_hint = (1, None)
        self.height = screen_size[1] / 15
        self.multiline = False
