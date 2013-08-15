import pyglet
from pyglet.window import key

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class Player:
    def __init__(self,x,y,image,horSpeed=1,maxGravSpeed=3):
        self.x = x
        self.y = y
        self.sprite = pyglet.sprite.Sprite(image,x=x,y=y)
        self.key_handler = key.KeyStateHandler()
        self.horSpeed = horSpeed
        self.maxGravSpeed = maxGravSpeed
        self.gravity = 0

    def gravitate(self):
        if self.y > 64:
            if self.gravity < self.maxGravSpeed:
                self.gravity += 0.05
        elif self.key_handler[key.SPACE] != True: self.gravity = 0

    def update(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.y -= self.gravity
        if self.key_handler[key.A]:
            self.x -= self.horSpeed
        if self.key_handler[key.D]:
            self.x += self.horSpeed
        if self.key_handler[key.SPACE]:
            self.gravity = -2
        self.gravitate()




    def draw(self):
        self.sprite.draw()