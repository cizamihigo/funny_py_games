import sqlite3 as sql

cccc = sql.connect('captalesduMonde/Countries.db')
ccc = cccc.cursor()
ccc.execute("DELETE FROM Countries.CapCountry")
def database():

    conn = sql.connect("captalesduMonde/Countries.db")

    Ccon =conn.cursor()
    # create a Table for country names and capital
    # Ccon.execute("CREATE TABLE CapCountry(Id INTEGER PRIMARY KEY AUTOINCREMENT,\
    #     CountryName VARCHAR(255) UNIQUE,\
    #     CapitalName VARCHAR(200))")

    #Ccon.execute("INSERT INTO CapCountry(CountryName, CapitalName) VALUES('India', 'New Dheli'),('China', 'Beijing'),('France', 'Paris'), ('Congo', 'Brazzaville')")
    conn.commit()
    Ccon.execute("SELECT CountryName,CapitalName FROM CapCountry")
    var = Ccon.fetchall()
    write_all = open("captalesduMonde/cap.txt",'w')
    for line in var:
        print(line)
        
        write_all.write(line[0] + ', ' + line[1] +'\n')
    # write_all.close()
        
    # for el in line:
    #     print(el)
def writting(CountryName, Cityname):
    co = sql.connect("captalesduMonde/Countries.db")

    cco = co.cursor()
    cco.execute("INSERT INTO CapCountry(CountryName,CapitalName) VALUES (?,?)",(CountryName, Cityname))
    co.commit()

    
