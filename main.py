import engine
import pyglet

playerImage = pyglet.image.load('resources/player.png')

window = pyglet.window.Window(640,480)
world = engine.World(640,480)
player = engine.Player(10,500,playerImage)

window.push_handlers(player.key_handler)

@window.event
def on_draw():
    window.clear()
    player.draw()

def update(dt):
    player.update()

pyglet.clock.schedule_interval(update,1.0/120.0)

pyglet.app.run()