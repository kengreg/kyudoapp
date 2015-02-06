'''
Created on Feb 5, 2015

@author: kengreg
'''
from django.test import TestCase


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)