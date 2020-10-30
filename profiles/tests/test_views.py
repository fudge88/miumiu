from django.test import TestCase
from django.urls import reverse
from profiles.models import UserProfile
from profiles.views import order_history, profile
from checkout.models import Order
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'xyz', 'xyz@thebeatles.com', '123456'
            )
        self.client.login(username='xyz', password='123456')

    def testProfile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_order_history(self):
        order = Order.objects.create(
            full_name='test'
            )

        print(order.order_number, order.full_name)

        response = self.client.get(
            f'/profile/order_history/{order.order_number}'
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
