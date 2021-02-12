import db
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    db.database()
    with open("captalesduMonde/cap.txt") as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split(',')
            wolrd[country] = city
def Write_to_file(capname, citname):
    db.writting(capname, citname)
    

print("Les Capitales des pays du Monde - Demander a votre Appli")
root = Tk()
root.withdraw()

wolrd ={}

read_from_file()
while True:
    q_country =simpledialog.askstring("Country AKILI", "Enter Countrie's Name: ")
    q_country = q_country.capitalize()
    q_country= str(q_country)
    # q_country[0] = q_country[0].upper()
    # dd = str(q_country)
    # print(dd)
    if q_country in wolrd:
        result = wolrd[q_country]
        messagebox.showinfo('Answer', 'The capital city of  ' + q_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me',
                                          'I dont\'t know! ' + 
                                          'what is the capital city of ' + q_country + ' ? ' )
        result = wolrd[q_country]
        if result == None:
            new_city ='NOT SPECIFIED'
        # db.writting(q_country,new_city)
        Write_to_file(q_country,new_city)
        read_from_file()
root.mainloop()