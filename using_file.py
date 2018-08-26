import sys
import os
import shutil
import time

poem = '''\
Programming is fun
When the work is done\
If you wanna make your work also fun:\
	use python!\
'''

f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt','r')
#line=f.read()
line = f.readline()
print(line)
line = f.readline()
print(line)
print('byte:%d' % len(line))
f.close()


	
os.system("pause")

