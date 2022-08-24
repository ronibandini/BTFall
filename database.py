# Worker Fall Detection v0.1
# database query
# Roni Bandini
# Aug 2022 Buenos Aires, Argentina

import sqlite3 as sl
import pandas , matplotlib.pyplot as plt
from termcolor import colored
import os
con = sl.connect('fall.db')

# with con:
#	con.execute('CREATE TABLE FALL (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, name TEXT);')

#sql = "INSERT INTO FALL (name) values ('Test')"

#with con:
#    con.execute(sql)

# Clearing the Screen
os.system('clear')

print(colored('Worker Fall Detection v0.1', 'green'))
print ("Roni Bandini - Argentina - ML Powered by Edge Impulse")
print ("")
print ("")
print("Previous falls")
print ("")

with con:
	data = con.execute("SELECT Timestamp, worker FROM FALL")

	for row in data:
		print( colored("    "+row[0], 'yellow'), colored(row[1],'yellow')  )

print ("")
print ("")

sql = "select worker, count(*) AS myCount FROM FALL GROUP BY worker"

data = pandas.read_sql(sql, con)

plt.bar(data.worker,data.myCount)

plt.title("Worker falls report")
plt.xlabel("Worker")
plt.ylabel("Falls")

plt.savefig('chart.png')
plt.show()
