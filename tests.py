'''
Created on Feb 5, 2015

@author: kengreg
'''
from django.test import TestCase
from django.core.urlresolvers import resolve
from librokyudo.views import home_page




class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve ('/')
        self.assertEqual(found.func, home_page)