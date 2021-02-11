import turtle as t
from random import randint, random
# size = 300
# points = 7
# angle = 180 - (180 / points)

# t.color('yellow')
# t.begin_fill()
# for star in range(points):
#     t.forward(size)
#     t.right(angle)
# t.end_fill()

def draw_stars(points, size, col, x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for st in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

# main page code
t.hideturtle()
t.Screen().title("night sky")

t.Screen().bgcolor('dark blue')
while True:
    ranPt = randint(2,5) * 2 + 1
    ransize = randint(10,50)
    rancol =(random(),random(),random())
    ranX = randint(-350,300)
    ranY = randint(-250, 250)
draw_stars(ranPt, ransize, rancol, ranX, ranY)
# t.Screen().mainloop()