import turtle as tl

def draw_fractal(scale):
    scaling = 3.0
    if scale >= 5:
        draw_fractal(scale / scaling)
        tl.right(90)
        draw_fractal(scale / scaling)
        tl.left(90)
        draw_fractal(scale / scaling)
        tl.left(90)
        draw_fractal(scale / scaling)
        tl.right(90)
        draw_fractal(scale / scaling)
    else:
        tl.forward(scale/1.01)

scale = 500

tl.delay(0.1)
tl.pensize(1)
tl.penup()
tl.goto(-scale*0.5, 0)
print(tl.screensize())
tl.pendown()

draw_fractal(scale)
tl.done()