# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from podcasteryapp.models import Slot, Read

class ReadAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['text', 'slot']}),
		('Date information', {'fields': ['date_created'], 'classes': ['collapse']}),
	]
	list_display = ('text', 'date_created', 'slot')
	search_fields = ['text']

class SlotAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['location', 'episode', 'show']}),
	]
	list_display = ('show', 'episode', 'location')
	list_filter = ['show', 'location']
	search_fields = ['show', 'episode']

admin.site.register(Slot, SlotAdmin)
admin.site.register(Read, ReadAdmin)