import os
settings_module = "%s.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
from django.test import TestCase
from mysite.main.models import Pages


class AnimalTestCase(TestCase):
    def setUp(self):
        Pages.objects.create(name="lion", sound="roar")
        Pages.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Pages.objects.get(name="lion")
        cat = Pages.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')