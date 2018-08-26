import sys
import os
#Function define
def say(message, times = 1):
	print (message * times)

say("hello")
say("world",5)
say("world",-5)
say(1,5)

os.system("pause")

