import csv
from collections import defaultdict

"""This is a script for creating the two diminsional dictionary that will hold the 
DNP3 data object library.  This will be used for reference when decrypting 
messages."""

"""
with open('DNP3 data object library.csv', newline = '') as csvfile:
	fileReader = csv.reader(csvfile, delimiter = ",", quotechar = '|')
	for row in fileReader:
		print(', '.join(row))
"""
"""This prints the current csv file"""
"""Also, to call this from the imported script, just import the script, then with the scripts name, call the method with scriptname.function(value) and it will work fine."""
"""
with open('DNP3 data object library.csv', newline = '') as DNP3:
	fileReader = csv.reader(DNP3)
	for row in fileReader:
		print(row)
"""

"""Create the 2D Dictionary. Load the dictionary with the csv file"""
"""
with open('DNP3 data object library.csv', newline = '') as DNP3:
	fileReader = csv.DictReader(DNP3)
	headers = fileReader.fieldnames
	DNP3dict = {row['Group']: row for row in fileReader}
"""
def buildDict():
	#method 1: read the values from the csv file, return the list of 
	#dicts to the method and then append them to a dictionary.
	#problem: It is only a 1 diminsional dictionary
	
	#list method, works but requires an index instead of a string for subset key
	"""
	listDict = csv.reader(open("DNP3 data object library.csv"))
	Dict = defaultdict(list)
	count = 1
	for row in listDict:
		#Dict.append(row)
		dict2 = dict()
		#groupPos = listDict[count][0]  
		#variationPos = listDict[count][1]
		#value = listDict[count][3]
		if count < 217:
			print('\n\n')
			print(count)
			lineX = row
			groupPos = lineX[0]
			variationPos = lineX[1]
			value = lineX[5]
			dict2[variationPos] = value
			Dict[groupPos].append(dict2)
			count = count + 1
			print(row)
		
	print(count)
	return Dict
	"""
	
	#method 2, works but only references the subset key, primary key is absent.
	#FIXED, WORKS for both primary and subkey
	listDict = csv.reader(open("DNP3 data object libraryV2.csv"))
	Dict = defaultdict(dict)
	count = 1
	for row in listDict:
		#Dict.append(row)
		dict2 = dict()
		#groupPos = listDict[count][0]  
		#variationPos = listDict[count][1]
		#value = listDict[count][3]
		if count < 217:
			print('\n\n')
			print(count)
			lineX = row
			groupPos = lineX[0]
			variationPos = lineX[1]
			value = lineX[5]
			dict2[variationPos] = value
			((x,y),) = dict2.items()
			Dict[groupPos].setdefault(x,[]).append(y)
			count = count + 1
			print(row)
		
	print(count)
	return Dict

	#with open('New DNP3 data object library.csv', mode = 'w') as outfile:
	#	writer = csv.writer(outfile)
	#	Dict = {rows[0]:rows[1] for rows in fileReader}
	#Dict = {'group'{'variation': row[0]} for row in fileReader}

	

# def build_dict(sourceFile):
	# project = defaultdict(dict)
	# headers = ['Group', 'Variation']
	# with open(sourceFile, 'rb') as DNP3:
		# readFile = csv.DictReader(DNP3, fieldNames = headers, dialect = 'excel')
		# for rowdict in readFile:
			# if None in rowdict:
				# del rowdict[None]
			# group = rowdict.pop("Group")
			# variation = rowdict.pop("Variation")
			# project[group][variation] = rowdict
	# return dict(project)
# sourceFile = 'DNP3 data object library.csv'
# print (build_dict(sourceFile))



	# Primary key is the group
	# Secondary key is the variation
	# Therefor, you would have something like...
	# d1 = {0:{209:1, 210:1, 211:1, 212:1...254:1}, 1:{1:1, 2:1}...end of dict}
	# The 0 is the group reference and primary key.
	# The 209 is the variation reference and secondary key.
	# The 1 is the value of that variation reference.
	

	
	