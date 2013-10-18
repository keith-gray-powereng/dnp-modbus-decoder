import csv
"""This is a script for creating the two diminsional dictionary that will hold the 
DNP3 data object library.  This will be used for reference when decrypting 
messages."""

"""
with open('DNP3 data object library.csv', newline = '') as csvfile:
	fileReader = csv.reader(csvfile, delimiter = ",", quotechar = '|')
	for row in fileReader:
		print(', '.join(row))
"""

with open('DNP3 data object library.csv', newline = '') as DNP3:
	fileReader = csv.reader(DNP3)
	for row in fileReader:
		print(row)

"""
def createDict(self):
"""	