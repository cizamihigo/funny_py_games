import random
import turtle as t
def cater():
    t.bgcolor('light green')

    cater.cterr = t.Turtle()
    cater.cterr.shape('square')
    cater.cterr.color('red')

    cater.cterr.speed(0)
    cater.cterr.penup()
    cater.cterr.hideturtle()
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
    cater.cterr.shapesize(1,cater_length, 1)
    cater.cterr.showturtle()
    display_score(score)
    place_leaf()

    while True:
        cater.cterr.forward(cater_speed)
        if cater.cterr.distance(leaf) < 20 :
            place_leaf()
            cater_length = cater_length + 1
            cater.cterr.shapesize(1,cater_length, 1)
            cater_speed = cater_speed + 1
            score = score + 10
            display_score(score)
        if out_window():
            game_over()
            break
t.onkey(start_game, 'space')
t.listen()
t.mainloop()