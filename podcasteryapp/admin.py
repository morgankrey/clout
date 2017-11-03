# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from podcasteryapp.models import Slot, Read, Show, Episode

class ReadAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['text']}),
		('Date information', {'fields': ['date_created'], 'classes': ['collapse']}),
	]
	list_display = ('text', 'date_created')
	search_fields = ['text']

class SlotAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['location', 'episode']}),
		('Read information', {'fields': ['read']}),
	]
	list_display = ('episode', 'location')
	list_filter = ['location']
	search_fields = ['episode']

class ShowAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title', 'producer']}),
	]
	list_display = ('title', 'producer')
	search_fields = ['title', 'producer']

class EpisodeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['show', 'title']}),
		('Date information', {'fields': ['release_date', 'read_close_date']}),
	]
	list_display = ('show', 'title')
	search_fields = ['show', 'title']

admin.site.register(Slot, SlotAdmin)
admin.site.register(Read, ReadAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)