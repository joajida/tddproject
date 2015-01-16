from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser=webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self,row_text):
		table=self.browser.find_element_by_id('id_list_table')
		rows=table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Let's visit this new website.
		self.browser.get(self.live_server_url)

		#The page's title and header mention To-Do lists.
		self.assertIn('To-Do',self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#We can enter a to-do item straight away.
		inputbox=self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		#We want to buy peacock feathers. Let's type it into a text box.
		inputbox.send_keys('Buy peacock feathers')

		#When we hit enter, we are taken to a new URL where "1: Buy peacock feathers" is an item in a to-do list.
		inputbox.send_keys(Keys.ENTER)
		list_url=self.browser.current_url

		self.assertRegex(list_url,r'/lists/.+')
		self.check_for_row_in_list_table("1: Buy peacock feathers")

		#We can add another item. Let's add "Use feathers to make a fly".
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys("Use feathers to make a fly")
		inputbox.send_keys(Keys.ENTER)

		#The page updates again and now lists both items.
		self.check_for_row_in_list_table("1: Buy peacock feathers")
		self.check_for_row_in_list_table("2: Use feathers to make a fly")

		#A new user visits the site
		self.browser.quit()
		self.browser=webdriver.Chrome()

		#When he visits the homepage, he sees no sign of our list
		self.browser.get(self.live_server_url)
		page_text=self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertNotIn('make a fly',page_text)

		#He starts a new list by entering an item
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		#He gets his own unique URL
		user_list_url=self.browser.current_url
		self.assertRegex(user_list_url,r'/lists/.+')
		self.assertNotEqual(user_list_url,list_url)

		#There is still no sign of our list
		page_text=self.browser.find_element_by_tag_name('body').text

		self.asserNotIn('Buy peacock feathers',page_text)
		self.assertNotIn('make a fly',page_text)

if __name__=='__main__':
	unittest.main(warnings='ignore')