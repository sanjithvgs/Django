from django.contrib import admin
#from django.conf.urls import url
from django.urls import include,path

urlpatterns = [
	path('', include('first.urls')),  
	path('admin/',admin.site.urls),
]


