# Worker Fall Detection v0.1
# database chart
# Roni Bandini
# Aug 2022 Buenos Aires, Argentina

import sqlite3, pandas , matplotlib.pyplot as plt
 
conn = sqlite3.connect("fall.db")
 
sql = "select worker, count(*) AS myCount FROM FALL GROUP BY worker"

data = pandas.read_sql(sql, con)

plt.bar(data.worker,data.myCount)

plt.title("Worker falls report")
plt.xlabel("Worker")
plt.ylabel("Falls")

plt.savefig('chart.png')
plt.show()