'''File: listBuild'''
'''Takes the user's input or specified text file and breaks it down into a list
of the individual messages (whether DNP3 or Modbus) which is then returned.
NOTE: if both input and a specified text file are provided, this module will
attempt to use the file first, but will default to the input if file input fails'''
import Report.py

def makeList(reportList):
	'''Currently assuming that it will be passed rep, which is a list of sperate messages'''
	outputString = '<ul class="collapsibleList" id="mahList">\n'
	
	for report in reportList: #loop through each Report report#= #FIGURE OUT IF LIST OR DUMMY HEAD
		#if report.description != "":
			#outputString += report.description
		#else:
		outputString += report.title + ": " + report.data
		outputString = innerContents(report.Next, outputString)
	#end for
	outputString += '\n</ul>'
	return outputString

def innerContents(reportList, outputString):
	'''description'''
	for item in reportList:
		outputString += "<li>\n"
		outputString += item.title + ": " + item.data + "\n"
		if item.description != "":
			outputString += "<li>\n" + item.description + "\n</li>\n</li>\n"
		else:
			outputString += "<ul>\n"
			outputString = innerContents(reportList.Next, outputString)
			outputString += "</ul>\n"
	#end for
	outputString += "</li>\n"
	return outputString