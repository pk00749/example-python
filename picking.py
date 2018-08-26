import sys
import os
import shutil
import time
import pickle as p

shopListFile = 'shoplist.txt'

shoplist = ['apple','mango','carrot']

f = open(shopListFile, 'wb')

p.dump(shoplist, f)

f.close()

del shoplist

f = open(shopListFile,'rb')

storedlist = p.load(f)

print (storedlist)

	
os.system("pause")

