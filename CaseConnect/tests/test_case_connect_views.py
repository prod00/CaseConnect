from django.test import TestCase
from case_connecting.models import User, Post
from django.utils import timezone
from django.urls import reverse

class TestUserPostListView(TestCase):
    def test_get_user_posts(self):
        post = Post()
        mike_user = User.objects.create(username="mikeobrien", password="mikey-2017!",
                                        email="mike@gmail.com", first_name="Mike", last_name="Obrien")
        post.recruiter = mike_user
        post.position = "TA"
        post.content = "Teaching assistant for MATH 201"
        post.knowledge = "MATH 201"
        post.pay = "$10 an hour"
        post.date_posted = timezone.now()
        post.save()

        url = reverse('user-posts', args=(post.recruiter.username,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)





