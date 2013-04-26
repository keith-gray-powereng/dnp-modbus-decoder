from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^index', views.index, name='index'),
	url(r'^dnp3/', views.dnp3, name='dnp3'), #Partially implemented
	url(r'^modbus/', views.modbus, name='modbus'), #Not implemented yet
	url(r'^auto/', views.auto, name='auto') #Not implemented yet
)