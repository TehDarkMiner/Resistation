import pyglet
from pyglet.window import key

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class Player:
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.sprite = pyglet.sprite.Sprite(image,x=x,y=y)
        self.key_handler = key.KeyStateHandler()

    def update(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        if self.key_handler[key.A]:
            self.x -= 1
            print 'a'


    def draw(self):
        self.sprite.draw()