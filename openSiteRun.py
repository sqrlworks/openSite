# openSiteRun.py - Opens user input/url(s) in user's default browser from the command line
# Functionaliy platform dependent - for Windows only

import sys, os, colorama
from colorama import Fore, Back, Style

colorama.init()

argv_len = len(sys.argv)

if argv_len < 2:
    print('Usage: py openSiteRun.py [urls] \nOpens urls in default browser')
    sys.exit()

if sys.platform.startswith('win'):
	print("\n1. Running on Windows: " + sys.platform)
	print ('2. Argument List: ' + str(sys.argv) + '\n')
	invalid_URL = []

	for i in range (1,argv_len):
		url = sys.argv[i]
		try:
			os.startfile(url)
		except:
			invalid_URL.append(url)

	if invalid_URL:
		print(Fore.WHITE + Back.RED + 'Error:' + Style.RESET_ALL+ ' Invalid URL for: ' + ', '.join(invalid_URL) +'\nMake sure to include ' + Fore.WHITE + Back.GREEN + 'prefix: www|http:|https:\n')

else:
	print("Functionality for Windows only")