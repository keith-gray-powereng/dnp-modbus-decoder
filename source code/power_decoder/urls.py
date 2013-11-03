from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^Power/DNP3/', include('DNP3.urls')),
	url(r'^Power/Modbus/', include('Modbus.urls')),
	url(r'^Power/Contact/$', 'power_decoder.views.contact'),
	url(r'^Power/About/$', 'power_decoder.views.about'),
    # Examples:
    # url(r'^$', 'power_decoder.views.home', name='home'),
    # url(r'^power_decoder/', include('power_decoder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
