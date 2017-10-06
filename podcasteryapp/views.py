from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'home.html')

def second(request):
	return HttpResponse('Second response')