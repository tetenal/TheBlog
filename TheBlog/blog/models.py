from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Post model is the actual blog post
# auto_now_add=true enables the server to grab today's date and time.

class Post(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    # This will allow the console to print out a value associated to the Post Model.
    # example model with title of Billy Bob would return "Billy Bob"
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))