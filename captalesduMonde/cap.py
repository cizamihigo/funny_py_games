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
