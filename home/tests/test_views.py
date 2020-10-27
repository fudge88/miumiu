from django.test import TestCase


class TestHomeViews(TestCase):

    def test_Index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_location(self):
        response = self.client.get('/location')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/map.html')
