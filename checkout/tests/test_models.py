from django.test import TestCase
from checkout.models import Order


class OrderTestCase(TestCase):
    def setUp(self):
        Order.objects.create(
            order_number=100, full_name='xyz', email='xyz@gmail.com',
            phone_number=99999999, country='England', order_total=500)
        Order.objects.create(
            order_number=101, full_name='xyz', email='xyz@gmail.com',
            phone_number=99999999, country='England', order_total=5000)

    def test_order(self):
        p1 = Order.objects.get(order_number=100)
        p2 = Order.objects.get(order_number=101)
        self.assertEqual(p1.order_total, 500)
        self.assertEqual(p2.order_total, 5000)
