import sqlite3 as lite
import sys
con = lite.connect('matrixbin.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS matrixbin_data")
    cur.execute("CREATE TABLE matrixbin_data( binary NUMERIC)")
    