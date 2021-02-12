import sqlite3 as sql

conn = sql.connect("captalesduMonde/Countries.db")

Ccon =conn.cursor()
# create a Table for country names and capital
# Ccon.execute("CREATE TABLE CapCountry(Id INTEGER PRIMARY KEY AUTOINCREMENT,\
#     CountryName VARCHAR(255) UNIQUE,\
#     CapitalName VARCHAR(200))")