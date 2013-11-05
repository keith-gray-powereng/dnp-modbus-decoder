"""This is a script for creating the two diminsional dictionary that will hold the 
DNP3 data object library.  This will be used for reference when decrypting 
messages."""

import csv
from collections import defaultdict


def buildDict():
	"""Function call when you want to create the dictionary, use 'item = buildDict()', the item returned will
	be a 2d dictionary where you can reference the data using item["0"]["209"] to return the description of that file.
	Primary key is the group
	Secondary key is the variation
	Therefore, you would have something like...
	d1 = {0:{209:1, 210:1, 211:1, 212:1...254:1}, 1:{1:1, 2:1}...end of dict}
	The 0 is the group reference and primary key.
	The 209 is the variation reference and secondary key.
	The 1 is the value of that variation reference."""

	#open the file
	listDict = csv.reader(open("DNP3 data object libraryV2.csv"))
	#create the primary dictionary which will hold the current group
	Dict = defaultdict(dict)
	#rule count
	#count = 1
	for row in listDict:		
		#create the subdictionary for the current variation of the group
		dict2 = dict()
		#pass the value for the values of the row
		lineX = row
		#group reference
		groupPos = lineX[0]
		#variation reference
		variationPos = lineX[1]
		#rule description, can be anything in the line, but at the moment is simply the description
		value = lineX[5]
		#Assign the value to the subdictionary with the variation reference
		dict2[variationPos] = value
		#assign the values of the subdictionary to x,y for appending to the primary dictionary
		((x,y),) = dict2.items()
		#append the x, y values to the primary dictionary
		Dict[groupPos].setdefault(x,[]).append(y)
		#count = count + 1
	return Dict


	

	
	