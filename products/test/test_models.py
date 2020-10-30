from django.test import TestCase
from products.models import Product, ProductReview, Category
from django.contrib.auth.models import User


class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(name="category")

    def test_category(self):
        c = Category.objects.get(name="category")
        self.assertEqual(c.name, 'category')


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product1", price=100, weight=100)
        Product.objects.create(name="product2", price=200, weight=100)

    def test_product(self):
        p1 = Product.objects.get(name="product1")
        p2 = Product.objects.get(name="product2")
        self.assertEqual(p1.price, 100)
        self.assertEqual(p2.price, 200)


class ProductReviewTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="product1", price=100, weight=100)
        Product.objects.create(name="product2", price=200, weight=100)
        user = User.objects.create_user(
            username='xyz', email='xyz@gmail.com', password='password')

        ProductReview.objects.create(Product=Product.objects.get(
            name='product1'), User=user,  review='ok')
        ProductReview.objects.create(Product=Product.objects.get(
            name='product2'), User=user,  review='ok')

    def test_product_review(self):
        p1 = ProductReview.objects.get(
            Product=Product.objects.get(name='product1'))
        p2 = ProductReview.objects.get(
            Product=Product.objects.get(name='product2'))
        self.assertEqual(p1.review, 'ok')
        self.assertEqual(p2.review, 'ok')
