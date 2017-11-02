# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

class Slot(models.Model):
	show = models.CharField(max_length=256)
	episode = models.CharField(max_length=256)
	location = models.IntegerField(default=1)

	def __str__(self):
		return self.show + ', ' + self.episode + ', ' + str(self.location)

class Read(models.Model):
	text = models.TextField(default='')
	date_created = models.DateTimeField('Date created', default=timezone.now)
	slot = models.ForeignKey(Slot, blank=True, null=True)

	def __str__(self):
		return self.text