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

		self.assertEqual(Read.objects.count(), 1)
		new_read = Read.objects.first()
		self.assertEqual(new_read.text, 'New read')

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'read_text': 'New read'})		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_save_reads_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Read.objects.count(), 0)

	def test_displays_all_reads(self):
		Read.objects.create(text='read 1')
		Read.objects.create(text='read 2')

		response = self.client.get('/')

		self.assertIn('read 1', response.content.decode())
		self.assertIn('read 2', response.content.decode())

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