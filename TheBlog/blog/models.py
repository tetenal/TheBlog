from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Post(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))