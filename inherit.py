import sys
import os
import time

class schoolMember:
	'''Represents any school member.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: %s)' % self.name)
		
	def tell(self):
		'''Tell my details.'''
		print('Name:"%s"   Age:"%s"' % (self.name, self.age))
		
class teacher(schoolMember):
	'''Represents a teacher.'''
	def __init__(self, name, age, salary):
		schoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Initialized Teacher: %s)' % self.name)
		
	def tell(self):
		schoolMember.tell(self)
		print('Salary:"%d"' % self.salary)
		
class student(schoolMember):
	'''Represents a student'''
	def __init__(self, name, age, marks):
		schoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student: %s)' % self.name)
	
	def tell(self):
		schoolMember.tell(self)
		print('Marks:"%d"' % self.marks)

t = teacher('Mrs. York', 40, 30000)
s = student('Li', 22, 90)

print

members = [t, s]
#members[0].tell()

for mem in members:
	mem.tell()
	
os.system("pause")

