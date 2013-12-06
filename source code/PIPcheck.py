"""PIP requirements check.
Checks if pip is installed, runs secondary script to execute pip"""
import os
try: 
	import pip
	os.system("PIPcheck.bat")
	os.system("pause")
except:
	print("Failed to find Pip, you must install Pip to use this application.")
