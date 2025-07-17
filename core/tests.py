from django.test import TestCase, Client
from .models import Contact
from django.urls import reverse_lazy

# Create your tests here.


class TestContactView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('contact') # /en/contact/
        cls.client = Client()

    def test_url(self):
        self.assertEqual(self.url, '/en/contact/')

    def test_response_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_response_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'contact.html')

    @classmethod
    def tearDownClass(cls):
        pass


class TestContactModel(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'first_name': 'John',
            'last_name' : 'Doe',
            'email' : 'john@example.com',
            'message' : 'TEst message'
        }
        cls.contact = Contact.objects.create(**cls.data)
    
    def test_create_model(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)

    @classmethod
    def tearDownClass(cls):
        pass