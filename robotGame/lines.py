import random
import turtle as t 

def get_len():
    choice =input("Enter line length (Long, Medium, Short): ")
    if choice == 'long':
        line_len = 100
    elif choice =='medium':
        line_len = 50
    else:
        line_len = 25
    return line_len
def get_wid():
    choice = input("Enter line width (superthick, thick, thin): ")
    if choice == 'superthick' :
        line_wdth = 20
    elif choice == 'thick':
        line_wdth = 10
    else: 
        line_wdth = 5
    return line_wdth

def inside_window():
    leftlimit = (-t.window_width()/2) + 100
    rightlimit = (t.window_width()/2) - 100
    top_limit = (t.window_height()/2) - 100
    bottom_limit = (-t.window_height()/2) + 100
    (x,y) = t.pos()
    inside = leftlimit < x < rightlimit and bottom_limit < y < top_limit
    return inside
def move(line_len):
    # pen_colors =['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    # t.pencolor(random.choice(pen_colors))
    t.colormode(255)
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)

    t.pencolor(red, blue, green)
    if inside_window():
        angle = random.randint(0,180)
        t.right(angle)
        t.forward(line_len)
    else:
        t.backward(line_len)
line_len = get_len()
line_width = get_wid()

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)
while True:
    move(line_len)
    # t.Screen().mainloop()


