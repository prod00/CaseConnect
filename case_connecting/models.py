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
        template = 'Recruiter: {0.recruiter}, Position: {0.position}, Post Date: {0.date_posted}'
        #return self.recruiter, self.position, self.date_posted.date()
        return template.format(self)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def getPosition(self):
        return self.position


class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = 'Applicant: {0.applicant}, Post: [{0.post}], Application Date: {0.date_applied}'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('case_connecting-applications')



class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = 'User: {0.user}, Post: [{0.post}]'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('case_connecting-home')

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    app = models.ForeignKey(Application, on_delete=models.CASCADE, default=None)
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        template = 'Sender: {0.sender}, Application: [{0.app}], Date Sent: {0.date_sent}'
        return template.format(self)

    def get_absolute_url(self):
        return reverse('case_connecting-chats')



