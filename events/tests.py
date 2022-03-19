from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LandingPageTests(TestCase):
    
    def test_Landing_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 302)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('events:home'))
        print("===" + str(response) + "\n")
        self.assertEquals(response.url, "/accounts/login/?next=/")