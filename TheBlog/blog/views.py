# from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
# from django.core.paginator import Paginator, InvalidPage, EmptyPage

from TheBlog.blog.models import *
from models import Post
from forms import PostForm, CommentForm

def post(request, pk):
	post = Post.objects.get(pk=pk)
	form = CommentForm(request.POST)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.save()
		return redirect(request.path)
	d = dict(post=post, form=form)
	d.update(csrf(request))
	return render_to_response("blog_detail.html", d,
							context_instance=RequestContext(request))

def main(request):

  posts = Post.objects.all()

  return render_to_response('blog_list.html', {'posts': posts})
