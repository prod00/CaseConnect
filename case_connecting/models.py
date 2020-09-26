from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    # things to add: deadline, how many people applied, user name
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    knowledge = models.CharField(max_length=200)
    content = models.TextField()
    pay = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.recruiter, self.position, self.date_posted.date()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

