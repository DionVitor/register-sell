from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.floatlayout import FloatLayout


class DefaultBoxLayout(BoxLayout):
    def __init__(self, screen_size, **kwargs):
        super(DefaultBoxLayout, self).__init__(**kwargs)

        with self.canvas:
            Color(.0902, .1960, .282353, 1)
            Rectangle(size=(screen_size[0], screen_size[1]))

        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10


class DefaultFloatLayout(FloatLayout):
    def __init__(self, screen_size, **kwargs):
        super(DefaultFloatLayout, self).__init__(**kwargs)

        with self.canvas:
            Color(.0902, .1960, .282353, 1)
            Rectangle(size=(screen_size[0], screen_size[1]))