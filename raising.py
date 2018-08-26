import sys
import os
import time

class shortIuputException(Exception):
	'''A user-defined exception class'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
		
try:
	s = input('Enter something -->')
	if len(s) <3:
		raise shortIuputException(len(s), 3)
	
except shortIuputException:
	print ('ShortInputException: The input was of length %d,\
 was expecting at least %d.'% (len(s), 3))
		
except EOFError:
	print('\nWhy did you do an EOF on me?')
except:
	print('\nSome error')
else:
	print('No exception was raised.')


os.system("pause")
