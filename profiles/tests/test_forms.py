from django.test import TestCase
from profiles.forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_user_profile_address_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))

    def test_address_form_not_required(self):
        valid_data = {
            'default_phone_number': '',
            'default_postcode': '',
            'default_town_or_city': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_county': '',
        }
        form = UserProfileForm(data=valid_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
