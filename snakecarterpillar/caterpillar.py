import random
import turtle as t

t.bgcolor('light green')

cterr = t.Turtle()
cterr.shape('square')
cterr.color('red')

cterr.speed(0)
cterr.penup()
cterr.hideturtle()

leaf = t.Turtle()
leaf_shape =((0,0),(14,2),(18,6),(20,20), (6,18), (2,14))

t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('white')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
    # leaf.mainloop()
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align= 'center',\
    font= ('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def out_window():
    pass
def game_over():
    pass
def display_score(current_score):
    pass
def place_leaf():
    pass
def start_game():
    global game_started
    if game_started :
        return
    game_started = True

    score = 0
    text_turtle.clear()

    cater_speed = 2
    cater_length = 3
    cterr.shapesize(1,cater_length, 1)
    cterr.showturtle()
    display_score(score)
    place_leaf()

    while True:
        cterr.forward(cater_speed)
        if cterr.distance(leaf) < 20 :
            place_leaf()
            cater_length = cater_length + 1
            cterr.shapesize(1,cater_length, 1)
            cater_speed = cater_speed + 1
            score = score + 10
            display_score(score)
        if out_window():
            game_over()
            break
t.onkey(start_game, 'space')
t.listen()
t.mainloop()