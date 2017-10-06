from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from podcasteryapp.views import index
from podcasteryapp.models import Read

class HomePageTest(TestCase):
	def test_index_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_post_request(self):
		response = self.client.post('/', data={'read_text': 'New read'})
		self.assertIn('New read', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

class ReadModelTest(TestCase):
	def test_saving_and_retrieving_reads(self):
		first = Read()
		first.text = 'First read'
		first.save()

		second = Read()
		second.text = 'Second read'
		second.save()

		saved_reads = Read.objects.all()
		self.assertEqual(saved_reads.count(), 2)

		first_saved = saved_reads[0]
		second_saved = saved_reads[1]
		self.assertEqual(first_saved.text, 'First read')
		self.assertEqual(second_saved.text, 'Second read')