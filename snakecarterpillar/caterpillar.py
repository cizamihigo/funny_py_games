import random
import turtle as t
def cater():
    t.bgcolor('light green')

    cterr = t.Turtle()
    cterr.shape('square')
    cterr.color('red')

    cterr.speed(0)
    cterr.penup()
    cterr.hideturtle()
def leaf():
    leaf = t.Turtle()
    leaf_shape =((0,0),(14,2),(18,6),(20,20), (6,18), (2,14))

    t.register_shape('leaf', leaf_shape)
    leaf.shape('leaf')
    leaf.color('white')
    leaf.penup()
    leaf.hideturtle()
    leaf.speed(0)
    # leaf.mainloop()
leaf()
cater()
t.mainloop()
