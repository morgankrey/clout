# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=1024, null=True, blank=True)
    date_created = models.DateTimeField('Date created', auto_now_add=True)
    date_updated = models.DateTimeField('Date updated', auto_now=True)

class Show(models.Model):
	title = models.CharField(max_length=256)
	producer = models.CharField(max_length=256)

	def __str__(self):
		return self.title

class Episode(models.Model):
	title = models.CharField(max_length=256)
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	release_date = models.DateTimeField('Release date')
	read_close_date = models.DateTimeField('Date when read copy closes')

	def __str__(self):
		return str(self.show) + ': ' + self.title

class Read(models.Model):
	text = models.TextField(default='')
	date_created = models.DateTimeField('Date created', auto_now_add=True)
	date_updated = models.DateTimeField('Date updated', auto_now=True)

	class Meta:
		permissions = (
				('view_read', "View read"),
				('edit_read', "Edit read"),
			)

	def __str__(self):
		return self.text

class Slot(models.Model):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
	location = models.IntegerField(default=1)
	read = models.ForeignKey(Read, blank=True, null=True)

	class Meta:
		permissions = (
				('view_slot_details', "View slot details"),
				('edit_slot', "Edit slot"),
			)
		unique_together = ('episode', 'location')

	def __str__(self):
		return str(self.episode) + ', ' + str(self.location)

# methods

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()