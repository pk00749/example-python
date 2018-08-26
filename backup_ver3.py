import sys
import os
import time

source = [r'C:\BAT\Template.txt', r'C:\BAT\NewBat.bat']

#source2 = r'C:\BAT\NewBat.bat'

target_dir = r'C:\BAT\\'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment -->')

if len(comment) == 0:
	target = today + os.sep + now + '.rar'
else:
	target = today + os.sep + now + '_' + comment.replace(' ','_') + '.rar'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory',today)

zip_command = "rar a %s %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print('Successful backup to',target)
else:
	print('Backup FAILED')

os.system("pause")

