

import csv
from collections import defaultdict

"""This is a script for creating the two diminsional dictionary that will hold the 
DNP3 data object library.  This will be used for reference when decrypting 
messages."""
def buildDict():
	"""function to build type dictionary,
	
	to get at a type with the returned dictionary, use
	returnedDict["groupNum"]["variationNum"]
	
	such as
	returnedDict["1"]["2"]
	
	keys are:
	group
	variation
	groupName
	variationName
	type
	description
	attributes
	
	attributes are 2 long tuples, (name , type)
	"""

	#open the file
	listDict = csv.reader(open("DNP3 data object libraryV2.csv"))
	#create the primary dictionary which will hold the current group
	Dict = dict()

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

		#I have no idea how this was working before without this.  This way is more proper...
		if not groupPos in Dict:
			Dict[groupPos] = dict()
		
		#pull attributes
		attribs = []
		place = 4
		while place + 2 < len(lineX):
			place += 2
			if place + 1 < len(lineX):
				attribs.append((lineX[place] + " " , lineX[place + 1]))
			

		#Assign the value to the subdictionary with the variation reference
		dict2["group"] = groupPos + " "
		dict2["variation"] = variationPos + " "
		dict2["groupName"] = GroupName + " "
		dict2["variationName"] = VariationName + " "
		dict2["type"] = type + " "
		dict2["description"] = description + " "
		
		dict2["attributes"] = list(attribs)
		
		Dict[groupPos][variationPos] = dict2
		
	return Dict
   
   
"""You shouldn't be using this, use one of the below instead"""
def fetchVariableSizeFieldTable(filename):
    listDict = csv.reader(open(filename))
    
    Dict = dict()
     
    for row in listDict:
    
        group = row[0]
        variation = row[1]
        valueIndex = row[2]
        valueSizeIndex = row[3]
    
        if not group in Dict:
            Dict[group] = dict()
        
        if not variation in Dict[group]:
            Dict[group][variation] = []
        
        Dict[group][variation].append((valueIndex, valueSizeIndex))
        
    return Dict()
        
def fetchUINTnTable():
    return fetchVariableSizeFieldTable("UINTn_variableSizeLookups.csv")
    
def fetchINTnTable():
    return fetchVariableSizeFieldTable("INTn_variableSizeLookups.csv")
    
def fetchVSTRnTable():
    return fetchVariableSizeFieldTable("VSTRn_variableSizeLookups.csv")
    
def fetchOSTRnTable():
    return fetchVariableSizeFieldTable("OSTRn_variableSizeLookups.csv")
