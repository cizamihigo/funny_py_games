# Start
import turtle as t
from itertools import cycle
import random
#  set the speed, background color, and pen size for the turtle
colors = cycle(['red','blue','yellow','green', 'purple','light blue', 'thistle','hot pink', 'goldenrod','seashell','lawn green', 'peru','gold','maroon','navy','aquamarine','lemon chiffon', 'peach puff', 'deep pink', 'misty rose'])
def draw_circles(size,angle,shift,shape):
    t.bgcolor(next(colors))
    next_shape =''
    if shape == 'circle':
        t.circle(size)
        next_shape ='square'
    elif shape == 'square':
        for count in range(0,4):
            t.forward(size +2 )
            t.left(90)
        next_shape ='circle'
    t.right(angle)
    t.forward(shift)
    draw_circles(size+ 4 , angle + 1 ,shift, next_shape)
    # t.pencolor(next(colors))
    # t.circle(size)
    # t.right(angle)
    # t.forward(shift)
    # draw_circles(size + 5 , angle + 1, shift + 1)
t.speed('fast')

t.pensize(4)

draw_circles(5,0,1,'circle')
