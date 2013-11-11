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
		#pull parts
		dict2 = dict()
		lineX = row
		
		#entries
		groupPos = lineX[0]
		variationPos = lineX[1]
		GroupName = lineX[2]
		VariationName = lineX[3]
		type = lineX[4]
		description = lineX[5]

		#pull attributes
		attribs = []
		place = 4
		while place + 2 < len(lineX):
			place += 2
			if place + 1 < len(lineX):
				attribs.append((lineX[place] + " " , lineX[place + 1]))
			

		#Assign the value to the subdictionary with the variation reference
		dict2["group"] = groupPos + " "
		dict2["variationPos"] = variationPos + " "
		dict2["GroupName"] = GroupName + " "
		dict2["VariationName"] = VariationName + " "
		dict2["type"] = type + " "
		dict2["description"] = description + " "
		
		dict2["attributes"] = list(attribs)
		
		Dict[groupPos][variationPos] = dict2
		
	return Dict


	

	
	