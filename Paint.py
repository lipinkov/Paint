from kivy.config import Config

Config.set('graphics', 'fullscreen', 'auto')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.slider import MDSlider
from kivymd.uix.tooltip import MDTooltip
from tkinter import filedialog
from tkinter import Tk
from PIL import Image

root = Tk()
root.withdraw()

class TooltipSlider(MDSlider, MDTooltip):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_enter=self.show_tooltip_with_delay)

    def show_tooltip_with_delay(self, *args):
        self.tooltip_text = 'Изменение размера'
        self.show_tooltip = True
        Clock.schedule_once(self.hide_tooltip, 2)

    def hide_tooltip(self, *args):
        self.tooltip_text = ''
        self.show_tooltip = False

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
            on_release: app.file_menu()
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
                on_press: app.minimize_app()
            Button:
                text: 'X'
                size_hint_x: None
                width: 30
                on_press: app.stop()
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
                font_name: 'Roboto-Bold'
                font_size: '16sp'
                size_hint_y: None
                height: 99.68
                on_release: root.ids.paint_widget.switch_to_brush()
            Button:
                text: 'Ластик'
                font_name: 'Roboto-Bold'
                font_size: '16sp'
                size_hint_y: None
                height: 99.68
                on_release: root.ids.paint_widget.switch_to_eraser()
            Button:
                text: 'Фигуры'
                font_name: 'Roboto-Bold'
                font_size: '16sp'
                size_hint_y: None
                height: 99.68
                on_release: app.open_shape_picker()
            Button:
                text: 'Палитра'
                font_name: 'Roboto-Bold'
                font_size: '16sp'
                size_hint_y: None
                height: 99.68
                on_release: app.open_color_picker()
            GridLayout:
                cols: 2
                size_hint_y: None
                height: 600.501
                Button:
                    background_normal: ''
                    background_color: 0.6, 0.2, 0.2, 1  # Темно-красный
                    on_release: app.change_color(0.6, 0.2, 0.2, 1)
                Button:
                    background_normal: ''
                    background_color: 0.2, 0.6, 0.2, 1  # Темно-зеленый
                    on_release: app.change_color(0.2, 0.6, 0.2, 1)
                Button:
                    background_normal: ''
                    background_color: 0.2, 0.2, 0.6, 1  # Темно-синий
                    on_release: app.change_color(0.2, 0.2, 0.6, 1)
                Button:
                    background_normal: ''
                    background_color: 0.6, 0.6, 0.2, 1  # Темно-желтый
                    on_release: app.change_color(0.6, 0.6, 0.2, 1)
                Button:
                    background_normal: ''
                    background_color: 0.6, 0.4, 0, 1  # Темно-оранжевый
                    on_release: app.change_color(0.6, 0.4, 0, 1)
                Button:
                    background_normal: ''
                    background_color: 0.4, 0, 0.4, 1  # Темно-фиолетовый
                    on_release: app.change_color(0.4, 0, 0.4, 1)
                Button:
                    background_normal: ''
                    background_color: 0, 0.4, 0.4, 1  # Темно-бирюзовый
                    on_release: app.change_color(0, 0.4, 0.4, 1)
                Button:
                    background_normal: ''
                    background_color: 0.4, 0.4, 0, 1  # Темно-оливковый
                    on_release: app.change_color(0.4, 0.4, 0, 1)
                Button:
                    background_normal: ''
                    background_color: 0.3, 0.3, 0.3, 1  # Серый
                    on_release: app.change_color(0.3, 0.3, 0.3, 1)
                Button:
                    background_normal: ''
                    background_color: 0.2, 0.2, 0.2, 1  # Темно-серый
                    on_release: app.change_color(0.2, 0.2, 0.2, 1)
                Button:
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # Белый
                    on_release: app.change_color(1, 1, 1, 1)
                Button:
                    background_normal: ''
                    background_color: 0.4, 0.2, 0, 1  # Темно-коричневый
                    on_release: app.change_color(0.4, 0.2, 0, 1)
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
        TooltipSlider:
            id: brush_size_slider
            min: 2  
            max: 10  
            value: 5  
            orientation: 'horizontal'
            size_hint_x: None
            width: 204  
            on_value: root.ids.paint_widget.change_brush_size(self.value)
            tooltip_text: 'Изменение размера'
        Label:
            size_hint_x: 1
        Label:
            id: cursor_position
            text: 'Координаты:'
            size_hint_x: None
            width: 200
            color: 0, 0, 0, 1
            halign: 'right'
"""

class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.line_width = 5
        self.color = (0, 0, 0, 1)
        self.eraser_mode = False
        self.drawing_shape = False
        self.shape = None
        self.shape_start_pos = None
        self.current_shape = None
        self.prev_pos = None
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

    def change_brush_size(self, size):
        self.line_width = size

    def switch_to_brush(self):
        self.eraser_mode = False
        self.color = self.saved_color
        self.drawing_shape = False

    def switch_to_eraser(self):
        self.eraser_mode = True
        self.saved_color = self.color
        self.color = (1, 1, 1, 1)
        self.drawing_shape = False

    def set_shape(self, shape):
        self.drawing_shape = True
        self.shape = shape
        self.color = self.saved_color

    def on_touch_down(self, touch):
        if touch.button != 'left':
            return False
        if self.collide_point(*touch.pos):
            touch.ud['in_bounds'] = True
            adjusted_pos = self._adjust_touch_pos(touch.x, touch.y)
            self.prev_pos = adjusted_pos
            if not self.drawing_shape:
                with self.canvas:
                    Color(*self.color)
                    touch.ud['line'] = Line(points=adjusted_pos, width=self.line_width)
            else:
                self.shape_start_pos = adjusted_pos
            return True
        else:
            touch.ud['in_bounds'] = False
            return False

    def on_touch_move(self, touch):
        if touch.button != 'left':
            return
        if touch.ud.get('in_bounds', False):
            x, y = self._adjust_touch_pos(touch.x, touch.y)
            if 'line' in touch.ud and not self.drawing_shape:
                if self.prev_pos:
                    points = [self.prev_pos[0], self.prev_pos[1], x, y]
                    with self.canvas:
                        Color(*self.color)
                        Line(points=points, width=self.line_width)
                self.prev_pos = (x, y)
            elif self.drawing_shape and self.shape_start_pos:
                self.update_current_shape(touch)
            return True

    def update_current_shape(self, touch, final=False):
        if self.shape_start_pos:
            start_x, start_y = self.shape_start_pos
            end_x, end_y = self._adjust_touch_pos(touch.x, touch.y)

            if self.shape == 'circle':
                dx = end_x - start_x
                dy = end_y - start_y
                radius = ((dx ** 2 + dy ** 2) ** 0.5 / 2)
                radius = min(radius, start_x - self.x - self.line_width, self.right - start_x - self.line_width,
                             start_y - self.y - self.line_width, self.top - start_y - self.line_width)

            if not final and self.current_shape:
                self.canvas.remove(self.current_shape)

            with self.canvas:
                Color(*self.color)
                if self.shape == 'circle':
                    self.current_shape = Line(circle=(start_x, start_y, radius), width=self.line_width)
                elif self.shape == 'rectangle':
                    self.current_shape = Line(rectangle=(
                        min(end_x, start_x), min(end_y, start_y), abs(end_x - start_x), abs(end_y - start_y)),
                        width=self.line_width)
                elif self.shape == 'line':
                    self.current_shape = Line(points=[start_x, start_y, end_x, end_y], width=self.line_width)

    def clear_canvas(self):
        self.update_canvas()

    def on_touch_up(self, touch):
        if touch.button != 'left':
            return
        if touch.ud.get('in_bounds', False):
            if self.drawing_shape and self.shape_start_pos:
                self.update_current_shape(touch, final=True)
                self.shape_start_pos = None
                self.current_shape = None
            self.prev_pos = None

    def _adjust_touch_pos(self, x, y):
        x = min(max(x, self.x + self.line_width), self.right - self.line_width)
        y = min(max(y, self.y + self.line_width), self.top - self.line_width)
        return x, y

class PaintApp(MDApp):
    def build(self):
        self.title = 'Paint Application'
        self.paint_widget = Builder.load_string(KV)
        self.paint_widget.ids.paint_widget.saved_color = (0, 0, 0, 1)
        Window.bind(mouse_pos=self.mouse_pos_callback)
        return self.paint_widget

    def mouse_pos_callback(self, instance, pos):
        if self.paint_widget.ids.paint_widget.collide_point(*pos):
            self.paint_widget.ids.cursor_position.text = f'Координаты: {int(pos[0])}, {int(pos[1])}'
        else:
            self.paint_widget.ids.cursor_position.text = 'Координаты:'

    def open_color_picker(self):
        color_picker = ColorPicker(color=self.paint_widget.ids.paint_widget.color)
        color_picker.bind(color=self.on_color)
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(color_picker)
        choose_button = Button(text='Выбрать', size_hint_y=None, height=50)
        choose_button.bind(on_release=lambda x: [popup.dismiss(), self.on_color(color_picker, color_picker.color)])
        popup_content.add_widget(choose_button)
        popup = Popup(title="Выберите цвет", content=popup_content, size_hint=(None, None), size=(400, 450))
        popup.open()

    def on_color(self, instance, value):
        self.paint_widget.ids.paint_widget.color = value
        self.paint_widget.ids.paint_widget.saved_color = value
        if self.paint_widget.ids.paint_widget.eraser_mode:
            self.paint_widget.ids.paint_widget.switch_to_brush()

    def change_color(self, r, g, b, a):
        self.paint_widget.ids.paint_widget.color = (r, g, b, a)
        self.paint_widget.ids.paint_widget.saved_color = (r, g, b, a)
        if self.paint_widget.ids.paint_widget.eraser_mode:
            self.paint_widget.ids.paint_widget.switch_to_brush()

    def open_shape_picker(self):
        content = BoxLayout(orientation='vertical')
        circle_button = Button(text='Круг', size_hint_y=None, height=50)
        rectangle_button = Button(text='Прямоугольник', size_hint_y=None, height=50)
        line_button = Button(text='Линия', size_hint_y=None, height=50)
        exit_button = Button(text='Выйти', size_hint_y=None, height=50)

        popup = Popup(title="Выберите фигуру", content=content, size_hint=(None, None), size=(300, 300))

        circle_button.bind(on_release=lambda x: [popup.dismiss(), self.set_shape('circle')])
        rectangle_button.bind(on_release=lambda x: [popup.dismiss(), self.set_shape('rectangle')])
        line_button.bind(on_release=lambda x: [popup.dismiss(), self.set_shape('line')])
        exit_button.bind(on_release=popup.dismiss)

        content.add_widget(circle_button)
        content.add_widget(rectangle_button)
        content.add_widget(line_button)
        content.add_widget(exit_button)

        popup.open()

    def set_shape(self, shape):
        self.paint_widget.ids.paint_widget.set_shape(shape)

    def minimize_app(self):
        Window.minimize()

    def file_menu(self):
        content = BoxLayout(orientation='vertical')
        save_button = Button(text='Сохранить', size_hint_y=None, height=78)
        load_button = Button(text='Загрузить', size_hint_y=None, height=78)
        cancel_button = Button(text='Отмена', size_hint_y=None, height=78)

        popup = Popup(title="Файл", content=content, size_hint=(None, None), size=(300, 300))

        save_button.bind(on_release=lambda x: [popup.dismiss(), self.save_drawing()])
        load_button.bind(on_release=lambda x: [popup.dismiss(), self.load_drawing()])
        cancel_button.bind(on_release=popup.dismiss)

        content.add_widget(save_button)
        content.add_widget(load_button)
        content.add_widget(cancel_button)

        popup.open()

    def save_drawing(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[("PNG files", "*.png"), ("BMP files", "*.bmp"), ("JPEG files", "*.jpeg"), ("All files", "*.*")]
        )
        if filepath:
            if filepath.endswith('.bmp'):
                self.paint_widget.ids.paint_widget.export_to_png(filepath)
                im = Image.open(filepath)
                im.save(filepath, 'BMP')
            elif filepath.endswith('.jpeg'):
                self.paint_widget.ids.paint_widget.export_to_png(filepath)
                im = Image.open(filepath)
                im.save(filepath, 'JPEG')
            else:
                self.paint_widget.ids.paint_widget.export_to_png(filepath)

    def load_drawing(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png"), ("BMP files", "*.bmp"), ("JPEG files", "*.jpeg"), ("All files", "*.*")]
        )
        if filepath:
            self.paint_widget.ids.paint_widget.canvas.clear()
            with self.paint_widget.ids.paint_widget.canvas.before:
                Color(1, 1, 1, 1)
                Rectangle(source=filepath, size=self.paint_widget.ids.paint_widget.size,
                          pos=self.paint_widget.ids.paint_widget.pos)

if __name__ == '__main__':
    PaintApp().run()