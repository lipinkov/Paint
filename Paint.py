from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line

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
            on_release: root.ids.paint_widget.clear_canvas()
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
            Button:
                text: 'Кисть'
                size_hint_y: None
                height: 99.68
                on_release: root.ids.paint_widget.switch_to_brush()
            Button:
                text: 'Ластик'
                size_hint_y: None
                height: 99.68
                on_release: root.ids.paint_widget.switch_to_eraser()
            GridLayout:
                cols: 2
                size_hint_y: None
                height: 600.501
                Button:
                    background_normal: ''
                    background_color: 0.6, 0.2, 0.2, 1  # Темно-красный
                Button:
                    background_normal: ''
                    background_color: 0.2, 0.6, 0.2, 1  # Темно-зеленый
                Button:
                    background_normal: ''
                    background_color: 0.2, 0.2, 0.6, 1  # Темно-синий
                Button:
                    background_normal: ''
                    background_color: 0.6, 0.6, 0.2, 1  # Темно-желтый
                Button:
                    background_normal: ''
                    background_color: 0.6, 0.4, 0, 1  # Темно-оранжевый
                Button:
                    background_normal: ''
                    background_color: 0.4, 0, 0.4, 1  # Темно-фиолетовый
                Button:
                    background_normal: ''
                    background_color: 0, 0.4, 0.4, 1  # Темно-бирюзовый
                Button:
                    background_normal: ''
                    background_color: 0.4, 0.4, 0, 1  # Темно-оливковый
                Button:
                    background_normal: ''
                    background_color: 0.3, 0.3, 0.3, 1  # Серый
                Button:
                    background_normal: ''
                    background_color: 0.2, 0.2, 0.2, 1  # Темно-серый
                Button:
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # Белый
                Button:
                    background_normal: ''
                    background_color: 0.4, 0.2, 0, 1  # Темно-коричневый
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
        self.line_width = 2
        self.color = (0, 0, 0, 1)
        self.eraser_mode = False
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

    def switch_to_brush(self):
        self.eraser_mode = False
        self.color = (0, 0, 0, 1)

    def switch_to_eraser(self):
        self.eraser_mode = True
        self.color = (1, 1, 1, 1)

    def clear_canvas(self):
        self.update_canvas()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            adjusted_pos = self.adjust_coords(touch.pos)
            with self.canvas:
                Color(*self.color)
                touch.ud['line'] = Line(points=adjusted_pos, width=self.line_width)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            adjusted_pos = self.adjust_coords(touch.pos)
            touch.ud['line'].points += adjusted_pos
        return super().on_touch_move(touch)

    def adjust_coords(self, pos):
        x, y = pos
        x = min(max(x, self.x + self.line_width), self.right - self.line_width)
        y = min(max(y, self.y + self.line_width), self.top - self.line_width)
        return x, y

class PaintApp(App):
    def build(self):
        self.title = 'Paint Application'
        self.paint_widget = Builder.load_string(KV)
        return self.paint_widget

if __name__ == '__main__':
    PaintApp().run()
