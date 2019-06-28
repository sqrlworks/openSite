# openSite_run.py - Opens user input: url in user's default browser from the command line
#Functionaliy platform dependent - for Windows only

import sys, os

argv_len = len(sys.argv)

if argv_len < 2:
    print('Usage: py openSite_run.py [urls] \nOpens urls in default browser')
    sys.exit()

if sys.platform.startswith('win'):
	print("1. Running on Windows: " + sys.platform)
	print ('2. Argument List: ' + str(sys.argv))
	invalid_URL = []

	for i in range (1,argv_len):
		url = sys.argv[i]
		try:
			os.startfile(url)
		except:
			invalid_URL.append(url)

	if invalid_URL:
		print('3. Error - Invalid URL for: ')
		print(*invalid_URL, sep=', ')
		print('Make sure to include prefix: www|http:|https:')

else:
	print("Functionality for Windows only")