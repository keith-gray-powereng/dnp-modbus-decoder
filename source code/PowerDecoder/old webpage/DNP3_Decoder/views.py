# Create your views here.
from django.http import HttpResponse #Needed?
from django.shortcuts import render, RequestContext, loader
import POC #Contains our DNP3 decoder module

def index(request):
	return render(request, 'DNP3_Decoder/basicTemplate.html')

def auto(request):
	return render(request, 'DNP3_Decoder/auto.html')

def dnp3(request):
	#if 'msg' in request.GET and request.GET['msg']:
	userData = request.GET['msg']
	decodedObj = POC.DNP3(str(userData))#("05 64 05 C0 01 00 0A 00")
	outty=[]
	for i in decodedObj:
		outty.append(str(i))
	#outty += str(i) + "</p>"
	#return HttpResponse(outty)
	return render(request, 'DNP3_Decoder/output.html', {'decodedStuff':outty, 'originalMsg':str(userData)}) #decodedObj = dictionary
	template = loader.get_template('DNP3_Decoder/output.html')
	context = RequestContext(request, {'decodedStuff':outty, 'originalMsg':str(userData)})
	return HttpResponse(template.render(context))

def modbus(request):
	return render(request, 'DNP3_Decoder/modbus.html')