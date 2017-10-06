from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from podcasteryapp.views import index

class HomePageTest(TestCase):
	def test_index_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')