# Start
import turtle as t
from itertools import cycle
#  set the speed, background color, and pen size for the turtle
t.speed('fast')
t.bgcolor('black')
t.pensize(1)


def draw_circles(size):
    t.pencolor('red')
    t.circle(size)
    draw_circles(size)

draw_circles(int(input("Enter the initial size:")))
