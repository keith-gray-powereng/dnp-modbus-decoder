# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from .parseInput import parseData
from .listBuild import *
from .DNPReportBuilder import *


def test(request):
    name = "Stephen Jarnagin"
    html = ("<html><body>Welcome {}, your test for basic html return worked. "
            "</body></html>".format(name))
    return HttpResponse(html)


def DNP3(request):
    return render_to_response('DNP3.html')


def DNP3results(request):
    # if 'msg' in request.GET and request.GET['msg']:
    # consider error-checking later
    userData = request.GET['inputByText']
    userFileContents = request.GET['fileContents']
    printBool = request.GET['printPass']

    # passing input into parseData to strip out the messages
    # (and get rid of extra data)
    messages = parseData(userData, userFileContents)
    # if it's not empty #example message = "05 64 05 C0 01 00 0A 00"
    if messages != "":
        decodedReports = []
        reportBuilder = DNPReportBuilder()

        #changing 3-part tuple -> (message, crc, request bool STRING)
        messages2 = []
        #Decoding each message and getting Report objects back
        for msg in messages:
            messages2.append(msg[0])

        decodedReports = reportBuilder.translate(messages2, True)
        #Convert Report list to HTML collapsible list

        if printBool == "false":
            outty = makeCollapsibleList(decodedReports)
        else:
            outty = makePrintableList(decodedReports)
    else:
        outty = 'Failed to parse out any messages'

    return render(
        request,
        'DNP3results.html',
        {'decodedStuff': outty})  # not using originalMessage for now
