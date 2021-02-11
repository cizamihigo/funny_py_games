import turtle as t

size = 300
points = 7
angle = 180 - (180 / points)

t.color('yellow')
t.begin_fill()
for star in range(points):
    t.forward(size)
    t.right(angle)
t.end_fill()
