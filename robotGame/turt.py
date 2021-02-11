import turtle as tur


def forme(vert, hori, color):
    tur.pendown()
    tur.shape('turtle')
    tur.speed("normal")
    # tur.setheading(90)

    tur.pensize(2)
    tur.color(color)
    tur.begin_fill()
    for i in range(1,3):
        tur.forward(vert)
        tur.right(90)
        tur.forward(hori)
        tur.right(90)
    tur.end_fill()
    tur.penup()
tur.penup()
tur.speed('normal')
tur.bgcolor('Dodger blue')
# frome(100,90,'GREEN')
# Design feet
tur.goto(-100,-150)
forme(50,20,'blue')
tur.goto(-30, -150)
forme(50,20,'blue')
# legs now
tur.goto(-25,-50)
forme(15,100,'yellow')
tur.goto(-55,-50)
forme(-15,100,'yellow')
# body
tur.goto(-90,100)
forme(100,150,'blue')
tur.goto(-50,50)
tur.pendown()
tur.pensize(1)
tur.color('Yellow')
tur.begin_fill()
tur.setheading(270)
tur.forward(20)
tur.right(20)
tur.setheading(45)
tur.backward(20)
tur.right(20)
tur.setheading(180)
tur.forward(20)
tur.right(20)
tur.setheading(180)
tur.backward(20)
tur.right(20)
tur.setheading(90)
tur.forward(20)
tur.right(20)
tur.setheading(235)
tur.backward(20)
tur.right(20)
tur.setheading(360)
tur.forward(20)
tur.right(20)

tur.end_fill()
tur.penup()
tur.setheading(0)
# arms
tur.goto(-150,70)
forme(60,15,'red')
tur.goto(-150,110)
forme(15,40,'red')

tur.goto(10,70)
forme(60,15,'red')
tur.goto(55,110)
forme(15,40,'red')

#neck
tur.goto(-50,120)
forme(15,20,'grey')
# head
tur.goto(-85,170)
forme(80,50,'red')

# eyes
tur.goto(-60,160)
forme(30,10,'white')
tur.goto(-55, 155)
forme(5,5,'black')
tur.goto(-40,155)
forme(5,5,'black')

# mouth

tur.goto(-65,135)
forme(40,5,'black')

tur.hideturtle()
# pause()