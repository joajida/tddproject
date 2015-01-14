from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser=webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Let's visit this new website.
		self.browser.get('http://localhost:8000')

		#The page's title and header mention To-Do lists.
		self.assertIn('To-Do',self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#We can enter a to-do item straight away.
		inputbox=self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		#We want to buy peacock feathers. Let's type it into a text box.
		inputbox.send_keys('Buy peacock feathers')

		#When we hit enter, the page updates and lists "peacock feathers" as a to-do item.
		inputbox.send_keys(Keys.ENTER)
		table=self.browser.find_element_by_id('id_list_table')
		rows=table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text=='1: Buy peacock feathers' for row in rows)
			)

		#We can add another item. Let's add "Use feathers to make a fly".
		self.fail('Finish the test!')

#The page updates again and now lists both items.

#An explanatory text points out that the website has generated a unique URL for that to-do list. 

#When we visit the URL, the to-do list is still there.

if __name__=='__main__':
	unittest.main(warnings='ignore')