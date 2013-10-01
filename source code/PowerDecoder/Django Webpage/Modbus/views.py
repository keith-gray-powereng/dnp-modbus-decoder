# Create your views here.
from django.shortcuts import render_to_response #renders template to the browser
from django.http import HttpResponseRedirect #redirect the browser to a different url
from django.contrib import auth 	#checks usernames/pws for logging in/out
from django.core.context_processors import csrf 	#web security, embed special code/token in forms, side step forge requests
import POC #Contains our DNP3 decoder module
import BitSlice

def Modbus(request):
	return render_to_response('modbus.html')
	
def modbusResults(request):
	return render_to_response('modbusResults.html')
	