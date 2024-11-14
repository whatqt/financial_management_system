from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class TestRegistrationUser(TestCase):
    def setUp(self):
        User.objects.create_user(username="unit_test", password="unit_test")

    def test_create_user(self):
        user = User.objects.get(username="unit_test")
        self.assertEqual(user.username, "unit_test")