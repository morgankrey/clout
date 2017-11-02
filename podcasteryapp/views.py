from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.http import Http404
from podcasteryapp.models import Read

def index(request):
	latest_read_list = Read.objects.order_by('-date_created')[:5]
	context = {
			'latest_read_list': latest_read_list
		}
	return render(request, 'index.html', context)

def read_detail(request, read_id):
	read = get_object_or_404(Read, pk=read_id)
	return render(request, 'reads/detail.html', {'read': read})

def slot_detail(request, slot_id):
    return HttpResponse("You're looking at slot %s." % slot_id)