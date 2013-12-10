# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic.base import TemplateView
import POC #Contains our DNP3 decoder module
from parseInput import parseData
from listBuild import *
from DNPReportBuilder import *

import BitSlice

def test(request):
	name = "Stephen Jarnagin"
	html = "<html><body>Welcome %s, your test for basic html return worked. </body></html>" % name
	return HttpResponse(html)
	
def DNP3(request):
	return render_to_response('DNP3.html')
	
def DNP3results(request):
	#if 'msg' in request.GET and request.GET['msg']: #consider error-checking later
	userData = request.GET['inputByText']
	userFileContents = request.GET['fileContents']
	printBool = request.GET['printPass']
	
	messages = parseData(userData, userFileContents) #passing input into parseData to strip out the messages (and get rid of extra data)
	if messages != "": #if it's not empty #example message = "05 64 05 C0 01 00 0A 00"
		decodedReports = []
		reportBuilder = DNPReportBuilder()
		
		#messages2 = [] #changing 3-part tuple -> (message, crc, request bool STRING)
		#for msg in messages: #Decoding each message and getting Report objects back
			#messages2.append( msg[0] )
			
		decodedReports = reportBuilder.translate(messages)
		#Convert Report list to HTML collapsible list
		
		if printBool == "false":
			outty = makeCollapsibleList(decodedReports)
		else:
			outty = makePrintableList(decodedReports)
	else:
		outty = 'Failed to parse out any messages'
		
	#outty = []
	#for i in decodedReports:
		#outty.append(str(i))
	return render(request, 'DNP3results.html', {'decodedStuff':outty}) #not using originalMessage for now
	