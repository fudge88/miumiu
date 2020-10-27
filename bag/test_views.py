from django.test import TestCase
from .contexts import bag_contents
from products.models import Product
from bag.views import shopping_bag, add_to_bag, edit_bag, remove_item


class TestBagViews(TestCase):

    def test_shopping_bag_view(self):
        response = self.client.get('/shopping_bag')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_item_to_bag(self):
        response = self.client.post('/add_to_bag/3')
        self.assertEqual(response.status_code, 302)

    def test_edit_bag_items(self):
        item = Product.objects.create(name='Test Product')
        response = self.client.post(f'/edit_bag/{item.id}')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'shopping_bag')

    def test_delete_bag_item(self):
        item = Product.objects.create(name='Test Product')
        response = self.client.post(f'/remove_item/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, 'shopping_bag')
        existing_items = Product.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
