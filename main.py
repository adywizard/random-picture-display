from random import randint
from math import sin, cos, pi
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty,\
    OptionProperty, ListProperty, StringProperty, BooleanProperty
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from kivy.clock import Clock
from kivy.app import App


Builder.load_string(
    """
#: import w kivy.core.window.Window

<Toolbar@FloatLayout>:
    size_hint_y: None
    height: 75
    canvas.before:
        Color:
            rgba: 1, 1, 1, .5
        Rectangle:
            pos: self.pos
            size: self.size


<Arrow>:
    canvas.before:
        Color:
            rgba: self.color
        SmoothLine:
            close: True
            width: self.lwidth
            circle:
                self.center_x, self.center_y, self._radius

<TrippleArrow>:
    direction: 'left'
    sh: None, 1
    aw: dp(56)
    ah: dp(0)
    Arrow:
        id: f
        size_hint: root.sh
        width: root.aw
        opacity: 0
        direction: root.direction
        color: root.color
    Arrow:
        id: s
        size_hint: root.sh
        width: root.aw
        opacity: 0
        direction: 'left'
        color: root.color
        direction: root.direction
    Arrow:
        id: t
        size_hint: root.sh
        width: root.aw
        opacity: 0
        direction: 'left'
        color: root.color
        direction: root.direction

# example of how to use

<CircleWidget>:
    canvas.before:
        Color:
            rgba: self.color
        SmoothLine:
            close: True
            circle:
                self.center_x, self.center_y, self.circ_size
            width: root.lwidth

<CircleLabel>:
    canvas.before:
        Color:
            rgba: self.color
        SmoothLine:
            close: True
            circle:
                self.center_x, self.center_y, self.texture_size[1]

<Example>:
    arr: arr
    ScreenOne:
        name: 'arrow_scr'
        on_enter:
            root._clock.cancel()
            root._clock = None
        id: one
        canvas.before:
            Color:
                rgba: 1, 1, 1, .5
            SmoothLine:
                close: True
                circle:
                    self.center_x, self.center_y, self.height / 4
        # Toolbar:
        #     id: toolbar
        #     pos_hint_y: None
        #     y: -75


        TrippleArrow:
            color: 1, 0, 0, .4
            id: tripple

        TrippleArrow:
            orientation: 'rl-tb'
            direction: 'right'
            color: 0, 1, 0, .4
            id: tripple_g

        TrippleArrow:
            orientation: 'tb-lr'
            sh: 1, None
            ah: dp(56)
            direction: 'up'
            color: .761, .761, .761, 1
            id: tripple_gr

        TrippleArrow:
            orientation: 'bt-lr'
            sh: 1, None
            ah: dp(56)
            direction: 'down'
            color: 1, 1, 0, 1
            id: tripple_y

        Arrow:
            direction: 'left'
            color: 1, 0, 0, 1
            lwidth: 1
            duration: .5
            size_hint: .1, .1
            transition: 'out_elastic'
            pos_hint: {'center_x': .125, 'center_y': .5}
            on_press: label.text = 'left arrow pressed'
            on_release:
                root.change_screen(self.direction, 'image_scr')
                arr.direction = 'right'

        Arrow:
            direction: 'right'
            transition: 'linear'
            color: 0, 1, 0, 1
            lwidth: self.width
            size_hint: .05, .05
            pos_hint: {'center_x': .875, 'center_y': .5}
            on_press: label.text = 'right arrow pressed'
            on_release:
                root.change_screen(self.direction, 'image_scr')
                arr.direction = 'left'

        Arrow:
            direction: 'up'
            size_hint: .075, .075
            lwidth: 2
            transition: 'out_quart'
            pos_hint: {'center_x': .5, 'center_y': .835}
            on_press: label.text = 'up arrow pressed'
            on_release:
                root.change_screen(self.direction, 'image_scr')
                arr.direction = 'down'

        Arrow:
            direction: 'down'
            color: 1, 1, 0, 1
            transition: 'out_sine'
            lwidth: 3
            size_hint: .125, .125
            pos_hint: {'center_x': .5, 'center_y': .165}
            on_press: label.text = 'down arrow pressed'
            on_release:
                root.change_screen(self.direction, 'image_scr')
                arr.direction = 'up'

        CircleLabel:
            id: label
            size: self.texture_size
            text_size: w.width / 6, w.height / 6
            halign: 'center'
            valign: 'middle'
            text: 'click on arrows'

        CircleWidget:
            id: planet
            size_hint: None, None
            size: 3, 3
            lwidth: self.width + 2
            color: planet_two.color
            # first_q_color: planet_two.first_q_color
            # second_q_color: planet_two.second_q_color
            # third_q_color: planet_two.third_q_color
            # forth_q_color: planet_two.forth_q_color
            r: w.height // 4 - self.height // 2
            originx: one.center[0]
            originy: one.center[1]

        CircleWidget:
            id: planet_two
            size_hint: None, None
            size: 4, 4
            r: label.texture_size[1]
            lwidth: self.width + 2
            color: .1, .1, 1, 1
            first_q_color: .761, .761, .761, 1
            second_q_color: 0, 1, 0, 1
            third_q_color: 1, 1, 0, 1
            forth_q_color: 1, 0, 0, 1
            originx: label.center[0]
            originy: label.center[1]
            velocity: .005

    Screen:
        name: 'image_scr'

        AsyncImage:
            id: img
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .9, .7
            source: root.source

        Arrow:
            id: arr
            on_release: root.change_screen(self.direction, 'arrow_scr')
            size_hint: .05, .05
"""
)


class ScreenOne(Screen):
    pass

    # toolbar_clock_hide = ObjectProperty(None, allownone=True)

    # toolbar_clock_show = ObjectProperty(None, allownone=True)

    # def on_touch_down(self, touch):
    #     Animation.cancel_all(app.root.ids.toolbar)
    #     if self.toolbar_clock_hide:
    #         self.toolbar_clock_hide.cancel()
    #     if app.root.ids.toolbar.y < 0:
    #         self.toolbar_clock_show = \
    # Clock.schedule_once(self.show_toolbar, 0)
    #     return super().on_touch_down(touch)

    # def on_touch_up(self, touch):
    #     if not app.root.ids.toolbar.collide_point(*touch.pos):
    #         self.toolbar_clock_hide = \
    # Clock.schedule_once(self.hide_toolbar, 3)
    #     return super().on_touch_up(touch)

    # def show_toolbar(self, *_):
    #     ani = Animation(y=0, d=.3)
    #     ani.start(app.root.ids.toolbar)

    # def hide_toolbar(self, _):
    #     ani = Animation(y=-75, d=.3)
    #     ani.start(app.root.ids.toolbar)


class CircleWidget(Widget):

    lwidth = NumericProperty(1.)

    circ_size = NumericProperty(15)

    r = NumericProperty(10)

    velocity = NumericProperty(.0006)

    originx = NumericProperty(Window.center[0])

    originy = NumericProperty(Window.center[1])

    color = ListProperty([1, 1, 1, 1])

    first_q_color = ListProperty([1, 1, 1, 1])

    second_q_color = ListProperty([1, 1, 1, 1])

    third_q_color = ListProperty([1, 1, 1, 1])

    forth_q_color = ListProperty([1, 1, 1, 1])

    transition_d = NumericProperty(2)

    forward = BooleanProperty(True)

    _anim = ObjectProperty(None, allownone=True)
    _radians = NumericProperty(pi*0.5)
    _first = False
    _red = False
    _third = False
    _forth = False
    _motion = False

    def on_kv_post(self, *_):
        self.start_stop()

    def update(self, dt=0):

        if not self._motion:
            self._motion = True

        if self.center_x > Window.width / 2\
                and self.center_y > Window.height / 2 and not self._first:

            self._first = True
            self._second = False
            self._third = False
            self._forth = False

            self.animate(color=self.first_q_color)

        elif self.center_x < Window.width / 2\
                and self.center_y > Window.height / 2 and not self._forth:

            self._first = False
            self._second = False
            self._third = False
            self._forth = True

            self.animate(color=self.forth_q_color)

        elif self.center_x < Window.width / 2\
                and self.center_y < Window.height / 2 and not self._third:

            self._first = False
            self._second = False
            self._third = True
            self._forth = False

            self.animate(color=self.third_q_color)

        elif self.center_x > Window.width / 2\
                and self.center_y < Window.height / 2 and not self._second:

            self._first = False
            self._second = True
            self._third = False
            self._forth = False

            self.animate(color=self.second_q_color)

        self._radians += self.velocity
        if self.forward:
            self.x = self.originx - cos(self._radians) * self.r
        else:
            self.x = self.originx + cos(self._radians) * self.r
        self.y = self.originy + sin(self._radians) * self.r

    def animate(self, color):
        self.ani = Animation(color=color, d=self.transition_d)
        self.ani.start(self)

    def start_stop(self):
        if self._anim is None:
            self._anim = Clock.schedule_interval(self.update, 0)
        else:
            self._anim.cancel()
            self._anim = None
            self._motion = False


class CircleLabel(Label):

    ani = ObjectProperty()
    clock = BooleanProperty(False)

    def on_touch_move(self, touch):

        if self.collide_point(*touch.pos):
            if touch.dx < 0:
                if not self.clock:
                    self.clock = True
                    app.root.ids.tripple.c = 0
                    app.root.ids.tripple.animate()
                self.animate(color=[1, 0, 0, 1])
                if self.x > -40:
                    self.x -= 5
            elif touch.dx > 0:
                if not self.clock:
                    self.clock = True
                    app.root.ids.tripple_g.c = 0
                    app.root.ids.tripple_g.animate()
                self.animate(color=[0, 1, 0, 1])
                if self.x < 40:
                    self.x += 5
            if touch.dy < 0:
                if not self.clock:
                    self.clock = True
                    app.root.ids.tripple_y.c = 0
                    app.root.ids.tripple_y.animate()
                self.animate(color=[1, 1, 0, 1])
                if self.y > -40:
                    self.y -= 5
            elif touch.dy > 0:
                if not self.clock:
                    self.clock = True
                    app.root.ids.tripple_gr.c = 0
                    app.root.ids.tripple_gr.animate()
                self.animate(color=[.761, .761, .761, 1])
                if self.y < 40:
                    self.y += 5
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.center = Window.center
        self.animate(color=[.761, .761, .761, 1])
        return super().on_touch_up(touch)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            for wid in self.parent.children:
                if isinstance(wid, CircleWidget):
                    wid.start_stop()
                    wid.update()
        return super().on_touch_down(touch)

    def animate(self, color):
        self.ani = Animation(color=color, d=.3)
        self.ani.start(self)


class Example(ScreenManager):

    source = StringProperty()

    arr = ObjectProperty()

    ani = ObjectProperty()

    fade_ani = ObjectProperty(None, allownone=True)

    _dir = StringProperty()

    _clock = ObjectProperty(None, allownone=True)

    def update_arrow_pos(self, *_, direction=''):

        if direction:
            self._dir = direction

        if self._dir == 'down':
            self.arr.color = 1, 1, 0, 1
            self.arr.pos = Window.width / 2 - Window.width * .025,\
                Window.height * .05

        elif self._dir == 'up':
            self.arr.color = .761, .761, .761, 1
            self.arr.pos = Window.width / 2 - Window.width * .025,\
                Window.height - Window.height * .1

        elif self._dir == 'left':
            self.arr.color = 1, 0, 0, 1
            self.arr.pos = Window.width * .05,\
                Window.height / 2

        elif self._dir == 'right':
            self.arr.color = 0, 1, 0, 1
            self.arr.pos = Window.width - Window.width * .1,\
                Window.height / 2

    def restore(self, *_):
        self.fade_ani = Animation(opacity=1, d=.3)
        self.fade_ani.start(self.ids.img)
        print('started 1')

    def update_image(self, *_):
        if self.ids.img.opacity == 0:
            self.ids.img.opacity = 1
        self.source =\
            f'https://picsum.photos/1600/1200?random={randint(0, 5000)}'

    def animate_image(self, *_):
        self.fade_ani = Animation(opacity=0, d=2)
        self.fade_ani.bind(on_complete=self.update_image)
        self.fade_ani.start(self.ids.img)

    def change_screen(self, direction, screen):

        if screen == 'image_scr':

            self.update_arrow_pos(direction=direction)

            self.source =\
                f'https://picsum.photos/1600/1200?random={randint(0, 5000)}'

            if not self._clock:
                self._clock = \
                    Clock.schedule_interval(self.animate_image, app.interval)

        self.transition.direction = direction
        self.current = screen


class Arrow(ButtonBehavior, Image):

    color = ListProperty([.761, .761, .761, 1])

    lwidth = NumericProperty(1.)

    duration = NumericProperty(.1)

    transition = OptionProperty(
        'linear', options=[
            'linear', 'out_elastic', 'out_back',
            'in_out_back', 'in_elastic', 'in_back',
            'in_bounce', 'in_out_bounce', 'in_out_expo',
            'out_quart', 'out_sine'
            ]
        )
    direction = OptionProperty(None, options=['left', 'right', 'up', 'down'])

    _anim = ObjectProperty()
    _radius = NumericProperty()
    _transition = StringProperty('linear')

    def on_transition(self, *args):
        self._transition = args[1]

    def on_direction(self, *args):

        if args[1] == 'right':
            self.source = 'images/arrow-right.png'
        elif args[1] == 'left':
            self.source = 'images/arrow-left.png'
        elif args[1] == 'up':
            self.source = 'images/arrow-up.png'
        elif args[1] == 'down':
            self.source = 'images/arrow-down.png'

    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos):
            if not self._radius:
                self._anim = Animation(
                    _radius=self.height*1.2, d=self.duration,
                    t=self._transition
                    )
                self._anim.start(self)
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):

        if self._radius:
            self._anim.cancel(self)
            self._radius = 0
        return super().on_touch_up(touch)


class TrippleArrow(StackLayout):

    c = NumericProperty(0)
    color = ListProperty([1, 1, 1, .5])
    size = ListProperty([.2, .2])

    def on_kv_post(self, *_):
        Clock.schedule_once(self.animate, 1)

    def animate(self, *_):
        ani = Animation(opacity=1, d=.2)
        ani.bind(on_complete=self.back_animate)

        if self.c == 0:
            ani.start(self.ids.t)
        elif self.c == 1:
            ani.start(self.ids.s)
        elif self.c == 2:
            ani.start(self.ids.f)

        self.c += 1

    def back_animate(self, *args):
        if self.c <= 3:
            ani = Animation(opacity=0, d=.2)
            ani.start(args[1])
            self.animate()
        if self.c == 3:
            self.c = -1
            app.root.ids.label.clock = False


class TestApp(App):

    interval = NumericProperty(15)

    def build(self):
        self.root = Example()
        self.root.transition.duration = .7
        Window.bind(on_resize=self.root.update_arrow_pos)


if __name__ == '__main__':
    Window.clearcolor = 16/255, 18/255, 21/255, 1
    if platform in ('win', 'linux', 'macos'):
        Window.size = 1200, 800
        Window.top = 100
        Window.left = 100
        Window.minimum_height = 600
        Window.minimum_width = 800
    app = TestApp()
    app.run()
