from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^decoder/', include('DNP3_Decoder.urls'))
	#url(r'^DNP3_Decoder/', include('DNP3_Decoder.urls')), #<- What tutorial says
	
	# Examples:
    # url(r'^$', 'PowerDecoder.views.home', name='home'),
    # url(r'^PowerDecoder/', include('PowerDecoder.foo.urls')),
)