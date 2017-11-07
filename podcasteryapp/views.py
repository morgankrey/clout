from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.http import Http404, HttpResponseForbidden
from django.utils import timezone

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from guardian.shortcuts import assign_perm, get_objects_for_user
from guardian.decorators import permission_required_or_403

from podcasteryapp.models import Read, Slot, Show, Episode
from podcasteryapp.forms import ReadForm, SlotForm, ShowForm

def index(request):
	latest_read_list = get_objects_for_user(request.user, 
											'view_read', 
											Read.objects.order_by('-date_created'))[:5]
	context = {
			'latest_read_list': latest_read_list
		}
	return render(request, 'index.html', context)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.address = form.cleaned_data.get('address')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm
	return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
	return render(request, 'profile.html', {})

@login_required
def show_new(request):
	if request.method == 'POST':
		form = ShowForm(request.POST)
		if form.is_valid():
			show = form.save(commit=False)
			show.user = request.user
			show.save()
			return redirect('show_detail', show_id=show.pk)
	else:
		form = ShowForm()
	return render(request, 'show_edit.html', {'form': form})

@login_required
def show_edit(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	if request.method == "POST":
		form = ShowForm(request.POST, instance=show)
		if form.is_valid():
			show = form.save(commit=False)
			show.save()
			return redirect('show_detail', show_id=show.pk)
	else:
		form = ShowForm(instance=show)
	return render(request, 'show_edit.html', {'form': form})

@login_required
def show_detail(request, show_id):
	show = get_object_or_404(Show, pk=show_id)
	return render(request, 'show_detail.html', {'show': show})

@permission_required_or_403('view_read')
def read_detail(request, read_id):
	read = get_object_or_404(Read, pk=read_id)
	return render(request, 'read_detail.html', {'read': read})

@login_required
def read_new(request):
	if request.method == 'POST':
		form = ReadForm(request.POST)
		if form.is_valid():
			read = form.save(commit=False)
			read.save()
			assign_perm('view_read', request.user, read)
			assign_perm('edit_read', request.user, read)
			return redirect('read_detail', read_id=read.pk)
	else:
		form = ReadForm()
	return render(request, 'read_edit.html', {'form': form})

@permission_required_or_403('edit_read')
@login_required
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

@login_required
def slot_detail(request, slot_id):
	slot = get_object_or_404(Slot, pk=slot_id)
	return render(request, 'slot_detail.html', {'slot': slot})

@login_required
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

@login_required
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