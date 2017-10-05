from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse('<html><title>Podcastery</title></html>')

def second(request):
	return HttpResponse('Second response')