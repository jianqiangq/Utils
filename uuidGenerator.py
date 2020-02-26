import uuid
import time

with open("uuid.txt", 'w') as f: 
	for i in range(24):
		f.write(str(i+1))
		f.write("\r\n")
		f.write(''.join(str(uuid.uuid1()).split('-')))
		f.write("\r\n")
		time.sleep(0.1)
	

