'''
Created on Feb 5, 2015

@author: kengreg
'''
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from librokyudo.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve ('/')
        self.assertEqual(found.func, home_page)   
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)