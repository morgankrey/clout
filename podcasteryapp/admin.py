# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from podcasteryapp.models import Slot, Read, Show, Episode, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'get_address')
    list_select_related = ('profile', )

    def get_address(self, instance):
        return instance.profile.address
    get_address.short_description = 'Address'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

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

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Read, ReadAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)