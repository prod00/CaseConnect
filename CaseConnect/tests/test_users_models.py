from django.test import TestCase
from users.models import Profile, User


class ProfileTest(TestCase):
    def test_fields(self):
        mike_user = User.objects.create(username="mikeobrien", password="mikey-2017!",
                                        email="mike@gmail.com", first_name="Mike", last_name="Obrien")
        profile = Profile()
        profile.id = 1
        profile.user = mike_user
        profile.save()

        record = Profile.objects.get(pk=1)
        self.assertEquals(record, profile)

