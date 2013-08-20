from django.contrib import admin
from TheBlog.blog.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)