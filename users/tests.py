from django.contrib.auth.models import User
from django.forms import models
from django.test import TestCase

# Create your tests here.
from CaseConnect.users.models import Profile


class TestUsersConfig(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_ready(self):
        print("Method: test_ready.")
        self.assertEqual()


class TestProfile(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_get_full_name(self):
        profile = Profile()
        profile.user = User.objects.create_user('User', 'last')
        profile.image = models.ImageField(default='default.jpg', upload_to='profile_pics')

        print("Method: test_get_full_name.")
        self.assertEqual(Profile.get_full_name(profile), "User last")

    def test_save(self):
        profile = Profile()
        profile.user = User.objects.create_user('User', 'last')
        profile.image = models.ImageField(default='default.jpg', upload_to='profile_pics')
        print("Method: test_save.")
        Profile.save(profile)
        self.assertTrue(Profile.image.output_size == (300, 300))
