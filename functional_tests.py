from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_get_on_homepage(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('Podcastery', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Podcastery', header_text)

		self.fail('Finish the test!')

if __name__=='__main__':
	unittest.main()