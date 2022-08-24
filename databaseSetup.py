# Database setup
# Run this script to create database file 

import sqlite3 as sl
con = sl.connect('fall.db')

with con:
	con.execute('CREATE TABLE FALL (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, name TEXT, worker TEXT);')


with con:
    con.execute(sql)

