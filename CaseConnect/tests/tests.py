from django.test import TestCase
from case_connecting.models import Post, Application, Save, User, Chat
from django.utils import timezone


class PostTest(TestCase):
    def test_user(self):
        mike_user = User.objects.create(username="mikeobrien", password="mikey-2017!",
                                        email="mike@gmail.com", first_name="Mike", last_name="Obrien")
        self.assertEquals(mike_user.username, "mikeobrien")

    def test_post(self):
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

        record = Post.objects.get(pk=1)
        self.assertEquals(record, post)


class ApplicationTest(TestCase):
    def test_user(self):
        alex_user = User.objects.create(username="alexrodriguez", password="alex-2018!",
                                        email="alex@gmail.com", first_name="Alex", last_name="Rodriguez")
        self.assertEquals(alex_user.username, "alexrodriguez")
    def test_application(self):
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

        mike_post = Post.objects.get(pk=1)

        application = Application()
        alex_user = User.objects.create(username="alexrodriguez", password="alex-2018!",
                                        email="alex@gmail.com", first_name="Alex", last_name="Rodriguez")
        application.applicant = alex_user
        application.message = "Hey Mike I want to be your TA"
        application.post = mike_post
        application.date_applied = timezone.now()
        application.save()

        record = Application.objects.get(pk=1)
        self.assertEquals(record, application)


class SaveTest(TestCase):
    def test_save(self):
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

        mike_post = Post.objects.get(pk=1)

        alex_user = User.objects.create(username="alexrodriguez", password="alex-2018!",
                                        email="alex@gmail.com", first_name="Alex", last_name="Rodriguez")

        save = Save()

        save.user = alex_user
        save.post = mike_post
        save.date_saved = timezone.now()
        save.save()

        record = Save.objects.get(pk=1)
        self.assertEquals(record, save)

class ChatTest(TestCase):
    def test_chat(self):
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
        mike_post = Post.objects.get(pk=1)

        application = Application()
        alex_user = User.objects.create(username="alexrodriguez", password="alex-2018!",
                                        email="alex@gmail.com", first_name="Alex", last_name="Rodriguez")
        application.applicant = alex_user
        application.message = "Hey Mike, I want to be your TA"
        application.post = mike_post
        application.date_applied = timezone.now()
        application.save()
        alex_application = Application.objects.get(pk=1)

        chat = Chat()
        chat.sender = mike_user
        chat.message = "Hey Alex, you are hired buddy!"
        chat.app = alex_application
        chat.date_sent = timezone.now()
        chat.save()

        record = Chat.objects.get(pk=1)
        self.assertEquals(record, chat)


