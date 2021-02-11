from tkinter import Tk, Canvas
from datetime import date, datetime
def get_events():
    list_events= []
    with open('CountDown/events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',') 
            event_date = datetime.strptime(current_event[0], '%d/%m/%y').date()
            current_event[0] = event_date
            list_events.append(current_event)

    return list_events
def date2date(date1, date2):
    time_elapsed = str(date1 -date2)
    nofdays = time_elapsed.split(' ')
    return nofdays[0]
root = Tk()
c = Canvas(root, width =800, height = 800, bg = 'black')
root.title("Countdown App")
c.pack()
c.create_text(200, 50, anchor = 'w', fill='orange', \
    font ='Arial 28 bold underline', text ="CountDown Application")
c.create_text(250,680, anchor = 'nw', fill = 'white' \
,font = 'Cambria 18 bold', text = "Made by @taketherisk11")

events = get_events()
today =date.today()

for event in events:
    event_name = event[0]
    day_till = date2date(event[0],today)
    display = 'It is %s days unitl %s' %(day_till, event_name)
    c.create_text(100,100,anchor='west', fill= 'light blue',\
        font = 'Times New Roman 19 bold', text = display)



root.mainloop()