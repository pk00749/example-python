import sys
import os
#Function define
def printMax(x,y):
	'''  Prints the maxium of two numbers.	
	The two values must be integers.'''
	x = int(x)
	y = int(y)
	
	if x > y:
		print(x,"is maxium")
	else:
		print(y,"is maxium")
		
printMax(2,3)
print (printMax.__doc__)

os.system("pause")

