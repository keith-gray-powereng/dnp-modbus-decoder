"""File: listBuild"""
"""Takes the user's input or specified text file and breaks it down into a list
of the individual messages (whether DNP3 or Modbus) which is then returned.
NOTE: if both input and a specified text file are provided, this module will
attempt to use the file first, but will default to the input if file input fails"""
import Report.py

def makeList(reportList):
	"""Currently assuming that it will be passed rep, which is a list of sperate messages"""
	myList = '<ul class="collapsibleList" id="mahList">\n'
	
	for msg in reportList: #loop through each Report msg#= #FIGURE OUT IF LIST OR DUMMY HEAD
		#if msg.description != "":
			#myList += msg.description
		#else:
		myList += msg.title + ": " + msg.data
		myList = innerContents(msg.Next, myList)
	#end for
	myList += '\n</ul>'
	return myList

def innerContents(reportList, myList):
	"""description"""
	for item in reportList:
		myList += "<li>\n"
		myList += item.title + ": " + item.data + "\n"
		if item.description == "":
			myList += "<li>\n" + item.description + "\n</li>\n</li>\n"
		else:
			myList += "<ul>\n"
			myList = innerContents(reportList.Next, myList)
			myList += "</ul>\n"
	#end for
	myList += "</li>\n"
	return myList