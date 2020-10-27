from django.test import TestCase
from products.forms import ProductReviewForm


class TestProductReviewForm(TestCase):

    def test_requiered_content(self):
        form = ProductReviewForm({'review': ''})
        self.assertTrue(form.is_valid)
