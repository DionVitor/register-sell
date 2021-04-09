from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatIconButton
from kivymd.uix.textfield import MDTextFieldRound

DEFAULT_FONT = 'default_font.ttf'


class DefaultButtonMenu(MDRectangleFlatIconButton):
    def __init__(self, **kwargs):
        super(DefaultButtonMenu, self).__init__(**kwargs)

        self.text_color = (1, 1, 1)
        self.size_hint = (.9, .12)


class DefaultTextInput(MDTextFieldRound):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultTextInput, self).__init__(**kwargs)

        self.font_size = screen_size[1] / 35
        self.size_hint = (.82, .08)
        self.multiline = False
        # self.normal_color = (1, 1, 1, 1) Change this attributes in framework!
        # self.color_active = (1, 1, 1, 1) Why have a issue in version: 0.104.2.dev0
        self.line_color = (.0902, .1960, .282353, 1)


class DefaultButton(MDRoundFlatButton):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultButton, self).__init__(**kwargs)

        self.size_hint = (.93, .08)
        self.text_color = (0.2, 0.8, 0.6, 1)


class DefaultHeadLabel(Label):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultHeadLabel, self).__init__(**kwargs)

        self.font_size = screen_size[1] / 22
        self.size_hint = (1, None)
        self.height = screen_size[1] / 4.5
        self.color = (1, 1, 1, 1)

        self.font_name = DEFAULT_FONT


class DefaultLabel(Label):
    def __init__(self, **kwargs):
        super(DefaultLabel, self).__init__(**kwargs)

        self.color = (1, 1, 1, 1)


class MenuLabel(Label):
    def __init__(self, screen_size: tuple, **kwargs):
        super(MenuLabel, self).__init__(**kwargs)

        self.color = (1, 1, 1, 1)
        self.text = 'Register Sell'
        self.font_size = screen_size[1] / 25
        self.height = screen_size[1] / 7
        self.text_size = (screen_size[0] - 100, None)


class DefaultPopup(Popup):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultPopup, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (screen_size[0] - 20, screen_size[1] / 2)
        self.auto_dismiss = False


class DefaultButtonForPopup(Button):
    def __init__(self, screen_size, **kwargs):
        super(DefaultButtonForPopup, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (screen_size[0] - 45, screen_size[1] / 12)

