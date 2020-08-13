from django.test import SimpleTestCase
from django.urls import reverse , resolve
from .views import index , nosotros
# Create your tests here.



class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_homepage_template(self): 
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/index.html')
    def test_homepage_contains_correct_html(self): 
        response = self.client.get('/')
        self.assertContains(response, 'Index')
    def test_homepage_does_not_contain_incorrect_html(self): 
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            index.as_view().__name__
        )
class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('nosotros')
        self.response = self.client.get(url)    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    def test_aboutpage_template(self): 
        self.assertTemplateUsed(self.response, 'pages/nosotros.html')       
    def test_aboutpage_contains_correct_html(self): 
        self.assertContains(self.response, 'Nosotros')
    def test_aboutpage_does_not_contain_incorrect_html(self): 
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/nosotros/')
        self.assertEqual(
            view.func.__name__,
            nosotros.as_view().__name__
        )