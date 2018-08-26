import sys
import os
ab = {'Swaroop' : 'swaroopch@163.com', 'Larry' : 'Larry@163.com', 'Matsumoto' : 'Matsumoto@163.com'}
print ("Swaroop's address is %s" % ab['Swaroop'])
ab['Guido'] = 'guido@163@.com'
del ab['Swaroop']
print ("\nThere are %d contacts in the address-book\n" % len(ab))

#Issue
for name, address in ab.item():
	print ("Contact %s at %s" % (name, address))
	
if 'Guido' in ab:
	print ("\nGuido's address is %s" % ab['Guido'])

os.system("pause")

