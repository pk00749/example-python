import sys
import os
import time

try:
	s = input('Enter something -->')
except EOFError:
	print('\nWhy did you do an EOF on me?')
	sys.exit()
except:
	print('\nSome error/exception occurred.')
	
print('Done')


os.system("pause")

