from django.urls import path

from . import views

urlpatterns =[
	path('',views.home, name="home"),
	path('add',views.add, name="add"),
	path('new',views.new, name="new"),
]
#	path('sam',views.sam, name="sam")
