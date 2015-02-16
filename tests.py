'''
Created on Feb 5, 2015

@author: kengreg
'''
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from librokyudo.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve ('/')
        self.assertEqual(found.func, home_page)   
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() 
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        #con este codigo se verifica si existe el correcto titulo en el codigo
        self.assertIn(b'<html lang="en">',response.content)
        self.assertIn(b'<title>Making my own website testing page</title>',response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))