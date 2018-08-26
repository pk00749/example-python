import sys
import os
import time

source = [r'C:\BAT\Template.txt', r'C:\BAT\NewBat.bat']

#source2 = r'C:\BAT\NewBat.bat'

target_dir = r'C:\BAT\\'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

zip_command = "rar a %s %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print('Successful backup to',target)
else:
	print('Backup FAILED')

os.system("pause")

