import sys
import os
#input("press")
num=23;
running = True;

while running:
	guess=int(input("pls enter an integer:"))
	if guess == num:
		print ('Congratuations, you guess it.')
		print ('Done')
		running = False
	elif guess < num:
		print ('lower.')
	else:
		print ('higher')	
else:
	print ("The while loop is over")
	
os.system("pause")

