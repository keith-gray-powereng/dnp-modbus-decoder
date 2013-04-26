# Create your views here.
from django.http import HttpResponse #Needed?
from django.shortcuts import render
import POC #Contains our DNP3 decoder module

def index(request):
	return render(request, 'DNP3_Decoder/basicTemplate.html')

def auto(request):
	return render(request, 'DNP3_Decoder/auto.html')

def dnp3(request):
	decodedObj = POC.DNP3("05 64 05 C0 01 00 0A 00")
	outty = ""
	for i in decodedObj:
		for l in i:
			outty += str(l) + " "
		outty += "</p>"
	return HttpResponse(outty)
	#return render(request, 'DNP3_Decoder/dnp3.html')

def modbus(request):
	return render(request, 'DNP3_Decoder/modbus.html')