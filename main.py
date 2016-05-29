import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty,\
ObjectProperty
from kivy.graphics import Color, Ellipse, Line, InstructionGroup, Point
from kivy.clock import Clock
from random import random



class MyBall(Widget):
    pass
    #def move(self, touch):
    #    self.pos = touch.x, touch.y
        
            
class MyTest(Widget):
    ball = ObjectProperty(None)
    app = ObjectProperty(None)
    #whiteline = InstructionGroup()
    lastErase = '1'
    
    
    def serve_ball(self):
        self.ball.center = self.center
    
    def on_touch_down(self, touch, *args):
        #whiteline = InstructionGroup()
        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        ud['color'] = random()
        pointsize = 5
        print('You touched me!')
        print(' - location touched: ', touch.x, touch.y)
        with self.canvas:
            Color(ud['color'], 1, 1, mode='hsv', group=g)
            #Color(0,1.,0) # green
            #Color(1.,1.,0) # yellow
            #d = 30.
            #MyBall(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            ud['line'] = [Point(points=(touch.x, touch.y), pointsize=8,
            group=g)]
            #touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)
            #noodle = touch.ud['line'] = Line(points=(touch.x, touch.y))
            #self.whiteline.add(noodle)
        if self.collide_point(*touch.pos):
            #touch.grab(self)
            #self.remove_widget(self.ball)
            #self.app.add_widget(self.ball)
            self.ball.center = touch.pos
            #return True
        if touch.is_double_tap:
            print('Touch is a double tap!')
            print(' - interval is', touch.double_tap_time)
            print(' - distance between previous is', touch.double_tap_distance)
            #self.canvas.clear() # works but clears everything
            #self.whiteline.get_group('whiteline')
            #self.whiteline.remove_group('line')
            #self.canvas.remove_group(ud['group'])
            # above doesn't work because it would only remove
            # the group, which doesn't yet have any points in it
            #self.canvas.remove_group('1') # removes group 1
            #print('last erase + g: ', self.lastErase, g)
            [self.canvas.remove_group(str(i)) for i in range(int(self.lastErase),
            int(g))] # erases marks since last erase
            self.lastErase = g # saves current group to use as start point
            # for subsequent erases
            
    def on_touch_move(self, touch):
        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        #self.ball.x = touch.x
        #self.ball.y = touch.y
        self.ball.center = touch.pos # ball follows cursor
        #touch.ud['line'].points += [touch.x, touch.y] # draws line
        #print(type(ud['line'][0]))
        ud['line'][0].add_point(touch.x, touch.y) # works
        #ud['line'].append(Point(points=(touch.x, touch.y),
        #pointsize=5, group=g))
        #print(ud['group'])
        #if ud['group'] == '5':
        #    self.canvas.remove_group(ud['group'])
        #    result is that it doesn't draw for group 5
            
    def update(self, dt):
        # call ball.move and other stuff
        #self.ball.move(Window.mouse_pos)
        pass
        #print Window.mouse_pos
        
    #def on_touch_move(self, touch):
    #    self.ball.center_x = touch.x
    #    self.ball.center_y = touch.y

            
class TestApp(App):
    icon = "./data/dumb_icon.png"
    title = "Draw with a Ball"
    clearbtn = ObjectProperty(None)

    def build(self):
        #parent = Widget()
        game = MyTest()
        #clearbtn = Button(text='Clear')
        #clearbtn.bind(on_release=self.clear_canvas)
        #parent.add_widget(self.game)
        #parent.add_widget(clearbtn)
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
        
    #def clear_canvas(self, obj):
    #    print("motherfucker")
    #    self.game.canvas.clear()


if __name__ == '__main__':
    TestApp().run()
