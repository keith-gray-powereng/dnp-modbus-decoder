# Create your views here.
from django.http import HttpResponse #Needed?
from django.shortcuts import render
#from POC import DNP3 #Contains our DNP3 decoder module


def index(request):
	return render(request, 'DNP3_Decoder/basicTemplate.html')
	
def auto(request):
	return render(request, 'DNP3_Decoder/auto.html')

def dnp3(request):
	#return HttpResponse(DNP3())
	return HttpResponse("Output Basic Decoded message here")
	#return render(request, 'DNP3_Decoder/dnp3.html')

def modbus(request):
	return render(request, 'DNP3_Decoder/modbus.html')
