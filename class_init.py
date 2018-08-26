import sys
import os
import time


class person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print('Hello, my name is', self.name)
	
p = person('York')
p.sayHi()

os.system("pause")

