from django.urls import resolve 
from django.test import TestCase #augmented version of the standard unittest.TestCase.
from django.http import HttpRequest

from lists.views import home_page #this should shows err since we dont have home_page in views.py

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Exercise One - Static Web Page</title>', html)
        self.assertIn('<h1 style="text-align: center;">Welcome to unlikely documents</h1>', html)
        self.assertIn('<p style="padding-left: 30px;">This static web page is meant to fulfill exercise one of PMPL</p>', html)
        self.assertIn('<p style="padding-left: 30px;">Ken Reinhart 2006507012</p>', html)
        self.assertTrue(html.startswith('</html>'))
        
