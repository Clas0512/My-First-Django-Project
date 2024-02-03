from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.utils import timezone
from django.db import models
import datetime


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()


#
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
