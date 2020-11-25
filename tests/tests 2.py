# import unittest
# import case_connecting
# from case_connecting.models import Post, Application, Save, User
# from django.utils import timezone
#
# class PostTest(unittest.TestCase):
#     def test_fields(self):
#         post = Post()
#         self.user = User.objects.create(username="mikeobrien", password="mikey-2017!",
#                                         email="mike@gmail.com", first_name="Mike", last_name="Obrien")
#         post.recruiter = self.user
#         post.position = "TA"
#         post.content = "Teaching assistant for MATH 201"
#         post.knowledge = "MATH 201"
#         post.pay = "$10 an hour"
#         post.date_posted = timezone.now
#         post.save()
#
#         record = Post.objects.get(pk=1)
#         self.assertEquals(record, post)
#

