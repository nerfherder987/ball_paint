import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty,\
ObjectProperty
from kivy.graphics import Color, Ellipse, Line, InstructionGroup, Point
from kivy.clock import Clock
from random import random



class MyBall(Widget):
    pass
        
            
class MyTest(Widget):
    ball = ObjectProperty(None)
    app = ObjectProperty(None)
    lastErase = '1'
    
    
    def serve_ball(self):
        self.ball.center = self.center
    
    def on_touch_down(self, touch, *args):
        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        ud['color'] = random()
        pointsize = 5
        with self.canvas:
            Color(ud['color'], 1, 1, mode='hsv', group=g)
            ud['line'] = [Point(points=(touch.x, touch.y), pointsize=8,
            group=g)]
        if self.collide_point(*touch.pos):
            self.ball.center = touch.pos
        if touch.is_double_tap:
            [self.canvas.remove_group(str(i)) for i in range(int(self.lastErase),
            int(g))] # erases marks since last erase
            self.lastErase = g # saves current group to use as start point
            # for subsequent erases
            
    def on_touch_move(self, touch):
        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        self.ball.center = touch.pos # ball follows cursor
        ud['line'][0].add_point(touch.x, touch.y)
            
    def update(self, dt):
        pass

            
class TestApp(App):
    icon = "./data/dumb_icon.png"
    title = "Draw with a Ball"

    def build(self):
        game = MyTest()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game



if __name__ == '__main__':
    TestApp().run()
