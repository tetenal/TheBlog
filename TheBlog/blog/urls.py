from django.conf.urls import *
from models import Post



# info = {
# 	'queryset': Post.objects.all(),
# }

urlpatterns = patterns('TheBlog.blog.views',
    (r"^(\d+)/$", "post"),
    
)
