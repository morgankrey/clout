from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'home.html', {
		'new_read_text': request.POST.get('read_text', '')
		})

def second(request):
	return HttpResponse('Second response')