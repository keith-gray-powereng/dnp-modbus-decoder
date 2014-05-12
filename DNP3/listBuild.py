'''File: listBuild'''
'''Takes a list of Report object that have already been decoded
and adds HTML code to them so that they can be displayed as a
collapsibleList object on the results page'''
from .Report import *

def makeCollapsibleList(reportList):
    '''Takes list of reports and adds HTML to the highest-level parts'''
    outputString = '<ul class="collapsibleList">\n'
    foundFunction = False
    #class="collapsibleList"

    for report in reportList.Next: #loop through each Report report in reportList
        #if report.description != "":
            #outputString += report.description
        #else:
        outputString += "<li>\n" + report.title + ":"
        for i in report.Next:
            if i.title.find("Sender") != -1: #Source
                outputString  += " Source: "
                if str(i.data) == "":
                    outputString += 'X'
                else:
                    outputString += str(i.data)
                outputString += ','
            elif i.title.find("Reciever") != -1: #Destination
                outputString += " Destination: "
                if str(i.data) == "":
                    outputString += 'X'
                else:
                    outputString += str(i.data)
                outputString += ','
            elif i.title.find("Transport") != -1: #Function Code
                for part in i.Next:
                    if part.title.find("Function") != -1:
                        foundFunction = True
                        outputString += ' ' + str(part.data) #" Function: "
        #end (i in report.Next) for loop
        if(foundFunction == False):
            for i in report.Next:
                if i.title.find("Control") != -1: #Message Control Data
                    for part in i.Next[0].Next:
                        if part.title.find("Function") != -1: #Function
                            outputString += ' Function: ' + str(part.data) #" Function: "
        outputString += "\n<ul>\n"
        if len(report.Next) > 0:
            outputString = innerContents(report.Next, outputString)
        outputString += "</ul>\n</li>\n"
    #end for
    outputString += '\n</ul>'
    return outputString

def makePrintableList(reportList):
    '''Takes list of reports and adds HTML to the highest-level parts'''
    outputString = '<ul>\n'

    for report in reportList.Next: #loop through each Report report in reportList
        #if report.description != "":
            #outputString += report.description
        #else:
        outputString += "<li>\n" + report.title + ": " + report.raw + "\n<ul>\n"
        if len(report.Next) > 0:
            outputString = innerContents(report.Next, outputString)
        outputString += "</ul>\n</li>\n"
    #end for
    outputString += '\n</ul><br><br>'
    return outputString

def innerContents(reportList, outputString):
    '''Adds HTML recursively to each sub-branch in the Report list's Report objects'''
    for item in reportList:
        if len(item.Next) > 0:
            outputString += "<li>\n" + item.title + ": " + str(item.data) + "\n"
            outputString += "<ul>\n"
            outputString = innerContents(item.Next, outputString)
            outputString += "</ul>\n</li>\n"
        else: #item.description
            #outputString += "<li>\n" + item.description + "\n</li>\n" #</li>\n
            outputString += '<li title="' + item.description + '">\n' + item.title + ": " + str(item.data) + "\n"
            #outputString += "" + item.description + "\n</li>\n"
    #end for
    return outputString
