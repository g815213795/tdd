from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):

        # found = resolve('/')
        # self.assertEqual(found.func, home_page)
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response,'home.html')

        # expected_html = render_to_string('home.html')
        # self.assertEqual(html,expected_html)
        # self.assertIn('<title>To-Do lists</title>', html)

        #self.assertTrue(html.endswith('</html>'))

# Create your tests here.
