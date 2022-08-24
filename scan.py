# Worker Fall Detection v0.1
# Scan BLE advertising, add to sqllite
# Roni Bandini
# Aug 2022 Buenos Aires, Argentina

# sudo apt install bluetooth libbluetooth-dev
# sudo apt-get install python3-pip
# pip3 install pybluez
# sudo apt-get install libbluetooth-dev bluez bluez-hcidump  libboost-python-dev libboost-thread-dev libglib2.0-dev
# sudo pip3 install gattlib
# sudo apt-get install bluetooth libbluetooth-dev
# sudo python3 -m pip install pybluez
# sudo pip3 install termcolor


from bluetooth.ble import DiscoveryService
from termcolor import colored
import sqlite3 as sl
import os
import time
import string
import re

con = sl.connect('fall.db')
cursor = con.cursor()

service = DiscoveryService()


found=0
iterations=0

# Clearing the Screen
os.system('clear')

print(colored('Worker Fall Detection v0.1', 'green'))
print ("Roni Bandini - Argentina - Powered by Edge Impulse")
print ("")

print("Scanning...")

while True:
	print("#"+str(iterations))

	devices = service.discover(2)

	for address, name in devices.items():

		if name!='':
		
			
			print( colored("    {}, {}".format(name, address), 'yellow'))

			if "Fall" in name:

				found=1

				print(colored('Fall detected', 'red'))

				# Create a regex pattern to match all special characters in string
				pattern = r'[' + string.punctuation + ']'
				# Remove special chars to avoid sql injection -> nameDb = re.sub(pattern, '', name)

				nameDb=name

				sql = "SELECT * from FALL WHERE name='"+nameDb+"'"
				print(sql)

				cursor.execute(sql)
				records = cursor.fetchall()

				if  len(records)==0:
					print('Adding record: '+name)

					fieldArray=name.split("-")
	
					sql = "INSERT INTO FALL (name, worker) values ('"+name+"','"+fieldArray[1]+"')"

					with con:
						con.execute(sql)
					time.sleep(5)

				else:
					print(colored('This fall was already in the database', 'green'))

		if found==0:
			print ("")
			print("No falls detected")

	iterations=iterations+1

	time.sleep(1)






		
