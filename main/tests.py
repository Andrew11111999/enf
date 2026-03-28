from django.test import TestCase
from django.apps import apps
from django.conf import settings


class BasicConfigTests(TestCase):
    def test_main_app_installed(self):
        self.assertIn('main', settings.INSTALLED_APPS)
        self.assertIsNotNone(apps.get_app_config('main'))

    def test_debug_flag_is_boolean_like(self):
        # Ensure DEBUG is a bool (loaded from env in settings)
        self.assertIn(type(settings.DEBUG), (bool, ))

# Create your tests here.
