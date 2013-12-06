"""PIP requirements check"""
import os
try: 
	import pip
	os.system("PIPcheck.bat")
	os.system("pause")
except:
	print("Failed to find Pip, you must install Pip to use this application.")
	
"""try:
	import django
except:
	print("Failed to find Django")
	return False
	
try:
	import bitstring
except:
	print("Failed to find bitstring")
	return False
"""