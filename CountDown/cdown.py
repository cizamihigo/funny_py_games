from tkinter import Tk, Canvas

root = Tk()
c = Canvas(root, width =800, height = 800, bg = 'black')
root.title("Countdown App")
c.pack()
c.create_text(200, 50, anchor = 'w', fill='orange', \
    font ='Arial 28 bold underline', text ="CountDown Application")
c.create_text(250,680, anchor = 'w', fill = 'white' \
,font = 'Cambria 18 bold', text = "Made by @taketherisk11")

root.mainloop()