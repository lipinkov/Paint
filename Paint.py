from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

KV = """
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: 30
        canvas.before:
            Color:
                rgba: 0.8, 0.8, 0.8, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Button:
            text: 'Файл'
            size_hint_x: None
            width: 100
        Button:
            text: 'Очистить'
            size_hint_x: None
            width: 100
        Label:
            text: 'Paint'
            color: 0.5, 0, 0.5, 1
            bold: True
            font_size: '20sp'
            size_hint_x: 0.6
            text_size: self.size
            halign: 'center'
            valign: 'middle'
        Widget:
            size_hint_x: None
            width: 60
        BoxLayout:
            size_hint_x: None
            width: 60
            Button:
                text: '–'
                size_hint_x: None
                width: 30
            Button:
                text: 'X'
                size_hint_x: None
                width: 30
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            id: tool_panel
            size_hint_x: None
            width: 200
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: 0.5, 0.5, 0.5, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
        PaintWidget:
            id: paint_widget
    BoxLayout:
        size_hint_y: None
        height: 50
        canvas.before:
            Color:
                rgba: 0.7, 0.7, 0.7, 1
            Rectangle:
                size: self.size
                pos: self.pos
"""

class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.update_canvas()

    def update_canvas(self):
        self.canvas.clear()
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_canvas_properties, pos=self.update_canvas_properties)

    def update_canvas_properties(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos

class PaintApp(App):
    def build(self):
        self.title = 'Paint Application'
        self.paint_widget = Builder.load_string(KV)
        return self.paint_widget

if __name__ == '__main__':
    PaintApp().run()