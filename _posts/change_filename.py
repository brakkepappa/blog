import os

for file in os.listdir():
	# jump over this file
	if file[0] == 'c':
		continue

	# Rename the wrong titled ones
	if file[14] == '-':
		# change this filename to not having this character
		os.rename(file, file[:14]+file[15:])
		print("Changed filename to "+file[:14]+file[15:])
	else:
		print(file)

	# Find files without dels in titles
	if file[16] != '-':
		# Rename single digit days
		if int(file[14]) >6:
			print(file[:15]+"-del1"+file[15:])
			os.rename(file, file[:15]+"-del1"+file[15:])
			
		# Rename rest of days
		else:
			print(file[:16]+"-del1"+file[16:])
			os.rename(file, file[:16]+"-del1"+file[16:])
