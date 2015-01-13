from selenium import webdriver
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
		self.fail('Finish the test!')

#We can enter an to-do item straight away.

#We want to buy peacock feathers. Let's type it into a text box.

#When we hit enter, the page updates and lists "peacock feathers" as a to-do item.

#We can add another item. Let's add "Use feathers to make a fly".

#The page updates again and now lists both items.

#An explanatory text points out that the website has generated a unique URL for that to-do list. 

#When we visit the URL, the to-do list is still there.

if __name__=='__main__':
	unittest.main(warnings='ignore')