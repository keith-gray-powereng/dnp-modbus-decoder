from django.shortcuts import render_to_response #renders template to the browser
from django.http import HttpResponseRedirect #redirect the browser to a different url
from django.contrib import auth 	#checks usernames/pws for logging in/out
from django.core.context_processors import csrf 	#web security, embed special code/token in forms, side step forge requests

def contact(request):
	return render_to_response('contact.html')
	
def about(request):
	return render_to_response('about.html')

	