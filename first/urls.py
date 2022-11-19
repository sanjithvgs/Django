from django.urls import path

from . import views

urlpatterns =[
	path('',views.home, name="home"),
	path('add',views.add, name="add"),
	path('new',views.new, name="new"),
	path('n_car',views.n_car, name="n_car"),
	path('service',views.service, name="service"),	
	path('locate',views.locate, name="locate"),
	path('contact',views.contact, name="contact"),

]
#	path('sam',views.sam, name="sam")
