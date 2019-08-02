# openSiteRun.py - Opens user input/url(s) in user's default browser from the command line
# Functionaliy platform dependent - for Windows only

import sys, os, time, colorama
from colorama import Fore, Back, Style

colorama.init()

argv_len = len(sys.argv)

if argv_len < 2:
    print('\nUsage: py openSiteRun.py [urls] \nOpens URLs in default browser\n')
    sys.exit()

if sys.platform.startswith('win'):

	invalid_URL = []

	for i in range (1,argv_len):
		url = sys.argv[i]
		try:
			os.startfile(url)
			time.sleep(3)
			print("\n1. Running on Windows: " + sys.platform)
			print ('2. Argument List: ' + str(sys.argv) + '\n')
		except:
			invalid_URL.append(url)

	if invalid_URL:
		print(Fore.WHITE + Back.RED + '\nError: Invalid URL for: ' + ', '.join(invalid_URL) 
			+ Style.RESET_ALL + '\nMake sure to include ' + Fore.WHITE + Back.BLACK + 'prefix: www|http:|https:\n')

else:
	print("Functionality for Windows only")