from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.http import Http404
from django.utils import timezone

from podcasteryapp.models import Read, Slot
from podcasteryapp.forms import ReadForm, SlotForm

def index(request):
	latest_read_list = Read.objects.order_by('-date_created')[:5]
	context = {
			'latest_read_list': latest_read_list
		}
	return render(request, 'index.html', context)

def read_detail(request, read_id):
	read = get_object_or_404(Read, pk=read_id)
	return render(request, 'read_detail.html', {'read': read})

def read_new(request):
	if request.method == 'POST':
		form = ReadForm(request.POST)
		if form.is_valid():
			read = form.save(commit=False)
			read.save()
			return redirect('read_detail', read_id=read.pk)
	else:
		form = ReadForm()
	return render(request, 'read_edit.html', {'form': form})

def read_edit(request, read_id):
	read = get_object_or_404(Read, pk=read_id)
	if request.method == "POST":
		form = ReadForm(request.POST, instance=read)
		if form.is_valid():
			read = form.save(commit=False)
			read.save()
			return redirect('read_detail', read_id=read.pk)
	else:
		form = ReadForm(instance=read)
	return render(request, 'read_edit.html', {'form': form})

def slot_detail(request, slot_id):
	slot = get_object_or_404(Slot, pk=slot_id)
	return render(request, 'slot_detail.html', {'slot': slot})

def slot_new(request):
	if request.method == 'POST':
		form = SlotForm(request.POST)
		if form.is_valid():
			slot = form.save(commit=False)
			slot.save()
			return redirect('slot_detail', slot_id=slot.pk)
	else:
		form = SlotForm()
	return render(request, 'slot_edit.html', {'form': form})

def slot_edit(request, slot_id):
	slot = get_object_or_404(Slot, pk=slot_id)
	if request.method == "POST":
		form = SlotForm(request.POST, instance=slot)
		if form.is_valid():
			slot = form.save(commit=False)
			slot.save()
			return redirect('slot_detail', slot_id=slot.pk)
	else:
		form = SlotForm(instance=slot)
	return render(request, 'slot_edit.html', {'form': form})