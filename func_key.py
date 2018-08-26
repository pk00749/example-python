import sys
import os
#Function define
def func(a,b=1,c=2):
	print ("a is",a,"and b is",b,"and c is",c)
	
func(3,7)
func(25,c=24)
func(c=50,a=100)

os.system("pause")

