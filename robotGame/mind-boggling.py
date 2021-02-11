# Start
import turtle as t
from itertools import cycle
import random
#  set the speed, background color, and pen size for the turtle
colors = cycle(['red','blue','yellow','green', 'purple','light blue', 'thistle','hot pink', 'goldenrod','seashell','lawn green', 'peru','gold','maroon','navy','aquamarine','lemon chiffon', 'peach puff', 'deep pink', 'misty rose'])
def draw_circles(size):
    t.pencolor(next(colors))
    t.circle(size)
    draw_circles(size + 6)
t.speed('fastest')
t.bgcolor('black')
t.pensize(1)

draw_circles(6)
