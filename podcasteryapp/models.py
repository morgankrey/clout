# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

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
	date_created = models.DateTimeField('Date created', default=timezone.now)

	def __str__(self):
		return self.text

class Slot(models.Model):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
	location = models.IntegerField(default=1)
	read = models.ForeignKey(Read, blank=True, null=True)

	def __str__(self):
		return str(self.episode) + ', ' + str(self.location)
