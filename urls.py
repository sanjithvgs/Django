from django.urls import path

from . import views

ur

urlpatterns =[
	path('',views.home, name="home"),
	path('add',views.add, name="add")
#	path('sam',views.sam, name="sam")
]