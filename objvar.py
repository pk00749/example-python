import sys
import os
import time

class person:
	'''Represents a person'''
	population = 0
	
	def __init__(self, name):
		'''Initializes the person's data'''
		self.name = name
		print('(Initializing %s)' % self.name)
		person.population += 1
		
	def __def__(self):
		'''I am dying'''
		print('%s say good bye' % self.name)
		person.population -= 1
		
		if person.population == 0:
			print('I am the last one')
		else:
			print('There are still %d people left' % person.population)
	def sayHi(self):
		print('Hello, my name is', self.name)
		
	def howMany(self):
		'''Print the current population'''
		if person.population == 1:
			print('I am the only person here')
		else:
			print('We have %d persons here' % person.population)
	
York = person('York')
York.sayHi()
York.howMany()

Li = person('Li')
Li.sayHi()
Li.howMany()

print('-------------')
York.howMany()
York.__def__()
York.howMany()
print('-------------')
Li.howMany()
Li.__def__()
Li.howMany()



os.system("pause")

