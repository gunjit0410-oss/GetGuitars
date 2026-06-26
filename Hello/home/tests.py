from django.test import TestCase, Client
from django.urls import reverse
from home.models import Contact, Guitar
import json

class GuitarAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test guitar instance
        self.guitar = Guitar.objects.create(
            name="Test Stratocaster",
            brand="Fender",
            price=50000,
            amazon_link="https://amazon.in/test",
            flipkart_link="https://flipkart.com/test"
        )

    def test_api_guitar_list(self):
        url = reverse('api_guitar_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Test Stratocaster")
        self.assertEqual(data[0]['brand'], "Fender")
        self.assertEqual(data[0]['price'], 50000)

    def test_api_guitar_detail_success(self):
        url = reverse('api_guitar_detail', args=[self.guitar.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['name'], "Test Stratocaster")
        self.assertEqual(data['brand'], "Fender")

    def test_api_guitar_detail_not_found(self):
        url = reverse('api_guitar_detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.content)
        self.assertIn('error', data)

    def test_api_guitar_list_method_not_allowed(self):
        url = reverse('api_guitar_list')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 405)


class ContactAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_contact_submit_success(self):
        url = reverse('api_contact_submit')
        payload = {
            'name': 'API User',
            'phone': '1234567890',
            'email': 'api@getguitars.com',
            'desc': 'Testing the native REST API endpoints'
        }
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertIn('id', data)
        # Verify db persistence
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'API User')

    def test_api_contact_submit_missing_fields(self):
        url = reverse('api_contact_submit')
        # Missing email field
        payload = {
            'name': 'API User Missing Email',
            'phone': '1234567890',
            'desc': 'Testing validation errors'
        }
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn('error', data)
        self.assertEqual(Contact.objects.count(), 0)

    def test_api_contact_submit_invalid_json(self):
        url = reverse('api_contact_submit')
        response = self.client.post(
            url,
            data="invalid-raw-text",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertIn('error', data)


class SearchViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test guitars
        Guitar.objects.create(
            name="Fender Precision Bass",
            brand="Fender",
            price=68999,
            image="https://unsplash.com/bass.jpg",
            amazon_link="https://amazon.com"
        )
        Guitar.objects.create(
            name="Yamaha FS80C Acoustic",
            brand="Yamaha",
            price=9490,
            image="https://unsplash.com/acoustic.jpg",
            amazon_link="https://amazon.com"
        )

    def test_search_view_success_match_name(self):
        url = reverse('search')
        response = self.client.get(url, {'query': 'Precision'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fender Precision Bass')
        self.assertNotContains(response, 'Yamaha FS80C Acoustic')

    def test_search_view_success_match_brand(self):
        url = reverse('search')
        response = self.client.get(url, {'query': 'Yamaha'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Yamaha FS80C Acoustic')
        self.assertNotContains(response, 'Fender Precision Bass')

    def test_search_view_no_query(self):
        url = reverse('search')
        response = self.client.get(url, {'query': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Products Found')

    def test_search_view_no_match(self):
        url = reverse('search')
        response = self.client.get(url, {'query': 'Gibson'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Products Found')
