'''
Created on Feb 1, 2015
@author: kengreg
'''
from selenium import webdriver
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
        self.browser.get('http://localhost:8000')
# The user will open an website/app in a browser
#To see it she open a browser
        self.assertIn('Gregory velez', self.browser.title)
        self.fail('Acabamos la prueba de esto')

#Crear un titulo de la pagina 
        if __name__ == '__main__':
            unittest.main(warnings='ignore')
#Aparece un login 

#Ahora al ingresar los datos se va a un profile


