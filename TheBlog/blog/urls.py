from django.conf.urls import *
from models import Post

urlpatterns = patterns('TheBlog.blog.views',
    (r"^(\d+)/$", "post"),
    (r'^month/(\d+)/(\d+)/$', 'month'),
    (r"^delete_comment/(\d+)/$", "delete_comment"),
	(r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
    
)
