import sys
import os
name = 'Swaroop'

if name.startswith('Swa'):
	print('Yes, the string start with "Swa"')
	
if 'a' in name:
	print('Yes, it contains the string "a"')
	
if name.find('war') != -1:
	print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print (delimiter.join(mylist))

os.system("pause")

