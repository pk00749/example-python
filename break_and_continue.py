import sys
import os
#For loop
while True:
	string = input("Enter String:")
	if 'quit' == string:
		break
	if len(string)<3:
		continue
	print ("Input is of sufficient length")
	
#os.system("pause")

