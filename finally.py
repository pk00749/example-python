import sys
import os
import time

try:
	f = open('poem.txt','r+')
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		time.sleep(2)
		#print(line,end="")#No wrap
		print(line)
finally:
	f.close()
	print('Cleaning up...closed the file')

os.system("pause")
