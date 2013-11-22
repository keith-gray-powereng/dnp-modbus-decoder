'''File: listBuild'''
'''Takes a list of Report object that have already been decoded
and adds HTML code to them so that they can be displayed as a
collapsibleList object on the results page'''
from Report import *

def makeCollapsibleList(reportList):
	'''Takes list of reports and adds HTML to the highest-level parts'''
	outputString = '<ul class="collapsibleList">\n'
	
	for report in reportList.Next: #loop through each Report report in reportList
		#if report.description != "":
			#outputString += report.description
		#else:
		outputString += "<li>\n" + report.title + ": " + report.data + "\n<ul>\n"
		if len(report.Next) > 0:
			outputString = innerContents(report.Next, outputString)
		outputString += "</ul>\n</li>\n"
	#end for
	outputString += '\n</ul>'
	return outputString

def innerContents(reportList, outputString):
	'''Adds HTML recursively to each sub-branch in the Report list's Report objects'''
	for item in reportList:
		outputString += "<li>\n"
		outputString += item.title + ": " + str(item.data) + "\n"
		if len(item.Next) > 0:
			outputString += "<ul>\n"
			outputString = innerContents(item.Next, outputString)
			outputString += "</ul>\n</li>\n"
		else: #item.description
			#outputString += "<li>\n" + item.description + "\n</li>\n" #</li>\n
			outputString += item.description + "\n</li>\n" #</li>\n
	#end for
	return outputString