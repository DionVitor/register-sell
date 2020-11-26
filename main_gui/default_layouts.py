from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle


class DefaultBoxLayout(BoxLayout):
    def __init__(self, screen_size, **kwargs):
        super(DefaultBoxLayout, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(size=(screen_size[0], screen_size[1]))

        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

