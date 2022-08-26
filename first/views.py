from django.shortcuts import render
from django.http import HttpResponse
from .models import destination
# Create your views here.
def home(request):

	det1=destination()
	det1.name="SANJITH VGS"
	return render(request, 'home.html',{'dam':det1})

def n_car(request):
	return render(request, 'newcar.html')

def service(request):
	return render(request, 'service.html')

def account(request):
	return render(request, 'account.html')

def contact(request):
	return render(request, 'contact.html')

def add(request):

	val1=request.POST["num1"]
	val2=request.POST["num2"]
	res = int(val1)+int(val2)
	return render(request, 'result.html',{'result':res})

def new(request):
	return render(request, 'new.html')

# New sample page for testing
#def sam(request):
#	return render(request, 'sample.html')
