from django.test import TestCase
from CaseConnect import case_connecting
import unittest
import pytest

from CaseConnect.CaseConnect import settings
from CaseConnect.case_connecting.models import *
from django.urls import reverse, resolve

from CaseConnect.case_connecting.models import *
from CaseConnect.case_connecting.views import *
# Create your tests here.


from django.urls import reverse

##from CaseConnect.case_connecting.models import Post
#from CaseConnect.case_connecting.views import UserPostListView, PostCreateView, PostUpdateView, PostDeleteView, \
  #  PostApplyView



class TestPostClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_get_Position(self):
        print("Method: test_get_absolute_url.")
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = models.DateTimeField(default=timezone.now)

        trial = Post.objects.get(pk=1)
        self.assertEqual(trial, post)


class TestUserPostListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_get_queryset(self):
        print("Method: test_get_queryset.")
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = "today"

        userPost = UserPostListView()
        userPost.model = post
        userPost.template_name = 'case_connecting/user_posts.html'
        userPost.context_object_name = 'posts'
        userPost.paginate_by = 8
        self.assertEqual(self, UserPostListView.get_queryset(userPost), userPost.objects)


class TestPostCreateView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_form_valid(self):
        postCreate = PostCreateView()
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = "today"
        postCreate.model = post
        postCreate.fields = ['position', 'knowledge', 'content', 'pay']

        print("Method: test_form_valid.")
        self.assertTrue(PostCreateView.form_valid(postCreate))


class TestPostUpdateView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_form_valid(self):
        postUpdate = PostUpdateView()
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = "today"
        postUpdate.model = post
        postUpdate.fields = ['position', 'knowledge', 'content', 'pay']
        print("Method: test_form_valid.")
        self.assertTrue(PostUpdateView.form_valid(postUpdate))

    def test_test_func(self):
        postUpdate = PostUpdateView()
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = "today"
        postUpdate.model = post
        postUpdate.fields = ['position', 'knowledge', 'content', 'pay']
        print("Method: test_test_func.")
        self.assertTrue(PostUpdateView.test_func(postUpdate))


class TestPostDeleteView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_test_func(self):
        postDelete = PostDeleteView()
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = "today"
        postDelete.model = post
        postDelete.success_url = '/'
        print("Method: test_test_func.")
        self.assertTrue(PostDeleteView.test_func(postDelete))


class TestPostApplyView(TestCase):
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_test_func(self):
        postApply = PostApplyView()
        post = Post()
        post.recruiter = "paul"
        post.position = "RA"
        post.knowledge = "Code"
        post.content = "research"
        post.pay = "100"
        post.date_posted = "today"
        postApply.model = post
        postApply.template_name = 'case_connecting/apply.html'

        print("Method: test_test_func.")
        self.assertTrue(PostApplyView.test_func(postApply))
