from django.test import TestCase
from django.urls import reverse
from products.models import Product
from bag.views import shopping_bag, add_to_bag, edit_bag, remove_item


class TestBagViews(TestCase):

    def test_shopping_bag_view(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_item_to_bag(self):
        item = Product.objects.create(
            name='Test Product', price=10, weight=10,
            description='pink', short_description='pink', directions='pink'
            )
        response = self.client.post(f'/bag/add/{item.id}/', {'quantity': '1'})
        self.assertEqual(response.status_code, 200)

    def test_edit_bag_items(self):
        item = Product.objects.create(name='Test Product', price=10, weight=10)
        response = self.client.post(f'/bag/edit/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, 'shopping_bag')

    def test_delete_bag_item(self):
        item = Product.objects.create(name='Test Product', price=10, weight=10)
        response = self.client.post(f'/bag/remove/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, 'shopping_bag')
        existing_items = Product.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
