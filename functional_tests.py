from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_read_table(self, row_text):
		table = self.browser.find_element_by_id('id_read_table')
		rows = table.find_elements_by_tag_name('tr')  
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_get_on_homepage(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('Podcastery', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Podcastery', header_text)

		inputbox = self.browser.find_element_by_id('id_new_read')  
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a read'
		)

		# She types "Pardon My Take 1/1/18" into a text box
		inputbox.send_keys('Pardon My Take 1/1/18')  

		# When she hits enter, the page updates, and now the page lists
		# "1: Pardon My Take 1/1/18" as an item in a reads bought table
		inputbox.send_keys(Keys.ENTER)  
		time.sleep(1)  
		self.check_for_row_in_read_table('1: Pardon My Take 1/1/18')

		inputbox = self.browser.find_element_by_id('id_new_read')  
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a read'
		)

		# She types "Pardon My Take 1/1/18" into a text box
		inputbox.send_keys('KFC Radio 1/1/18')  

		# When she hits enter, the page updates, and now the page lists
		# "1: Pardon My Take 1/1/18" as an item in a reads bought table
		inputbox.send_keys(Keys.ENTER)  
		time.sleep(1)  
		self.check_for_row_in_read_table('2: KFC Radio 1/1/18')

if __name__=='__main__':
	unittest.main()