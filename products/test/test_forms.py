from django.test import TestCase
from products.forms import ProductReviewForm, ProductForm


class TestProductReviewForm(TestCase):

    def test_requiered_content(self):
        form = ProductReviewForm({'review': ''})
        self.assertTrue(form.is_valid)

    def test_requiered_product(self):
        form = ProductForm({'name': ''})
        self.assertTrue(form.is_valid)
