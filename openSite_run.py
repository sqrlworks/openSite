# openSite_run.py - Opens user input: url in user's default browser from the command line
#Functionaliy platform dependent - for Windows only

import sys, os

if len(sys.argv) < 2:
    print('Usage: py openSite_run.py [url] \nOpens url in default browser')
    sys.exit()

print ('Argument List: ' + str(sys.argv))
url = sys.argv[1]

if sys.platform.startswith('win'):
	try:
		os.startfile(url)
		print("Running on Windows: " + sys.platform)
	except:
		print("Error: Invalid URL")
else:
	print("Functionality for Windows only")