# pip install hg+https://pyglet.googlecode.com/hg/
# pip install nodebox-opengl

# http://www.cityinabottle.org/nodebox/#introduction
from nodebox.graphics import *
import firefly

w, h = 600, 400
fireflies = firefly.make_flies(w, h)


def draw(canvas):
    for f in fireflies.flat:
        f.update()

    background(0)

    for f in fireflies.flat:
        f.draw()

    fill(.4)
    font("Helvetica", 20)
    text(str(canvas.frame % firefly.cycle_time), 20, 20)

def main():
    canvas.fps = 30
    canvas.size = w, h
    #canvas.fullscreen = True
    canvas.run(draw)

if __name__ == '__main__':
    main()
