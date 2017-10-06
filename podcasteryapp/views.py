from django.shortcuts import render, HttpResponse, redirect
from podcasteryapp.models import Read

def index(request):
	if request.method == 'POST':
		Read.objects.create(text = request.POST['read_text'])
		return redirect('/')
	
	reads = Read.objects.all()
	return render(request, 'home.html', {'reads': reads})

def second(request):
	return HttpResponse('Second response')