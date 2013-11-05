from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^test/$', 'DNP3.views.test'),
	url(r'^DNP3/$', 'DNP3.views.DNP3'),
	url(r'^DNP3results/$', 'DNP3.views.DNP3results'),
	# url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),
	
	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #rl(r'^admin/', include(admin.site.urls)),
)