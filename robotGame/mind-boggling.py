# Start
import turtle as t
from itertools import cycle
import random
#  set the speed, background color, and pen size for the turtle
colors = cycle(['red','blue','yellow','green', 'purple','light blue', 'thistle','hot pink', 'goldenrod','seashell','lawn green', 'peru','gold','maroon','navy','aquamarine','lemon chiffon', 'peach puff', 'deep pink', 'misty rose'])
def draw_circles(size,angle,shift):
    t.bgcolor(next(colors))
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circles(size + 5 , angle + 1, shift + 1)
t.speed('fast')

t.pensize(40)

draw_circles(5,0,1)
