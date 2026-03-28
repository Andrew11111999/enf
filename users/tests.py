from django.test import TestCase
from django.conf import settings


class AuthModelTests(TestCase):
    def test_custom_user_model_is_set(self):
        self.assertEqual(settings.AUTH_USER_MODEL, 'users.CustomUser')

# Create your tests here.
