import sqlite3
import sys
conn=sqlite3.connect('matrixbin.db')
curs=conn.cursor()
# function to insert data on a table
def add_data (temp, hum):
    curs.execute("INSERT INTO matrixbin_data values(datetime('now'), (?), (?))", (temp, hum))
    conn.commit()
# call the function to insert data
add_data (1,)
add_data (0,)
add_data (1,)
add_data (0,)
# print database content
print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM matrixbin_data"):
    print (row)
# close the database after use
conn.close()