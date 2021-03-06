'''
Created on Feb 1, 2015
@author: kengreg
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
#browser = webdriver.Chrome()
#browser.get('http://localhost:8000')


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User open the homepage
        self.browser.get('http://localhost:8000')
        # User looks for expected title
        self.assertIn('Making my own website testing page', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Making my own website testing page', header_text)
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a value')
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "aparece un nuevo item en la tabla")
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main()