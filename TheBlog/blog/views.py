import time
from calendar import month_name
# from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

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
	d = dict(post=post, form=form, user=request.user)
	d.update(csrf(request))
	return render_to_response("blog_detail.html", d,
							context_instance=RequestContext(request))

def delete_comment(request, post_pk, pk=None):
    """Delete comment(s) with primary key `pk` or with pks in POST."""
    if request.user.is_staff:
        if not pk: pklst = request.POST.getlist("delete")
        else: pklst = [pk]

        for pk in pklst:
            Comment.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse("TheBlog.blog.views.post", args=[post_pk]))

def mkmonth_lst():
    """Make a list of months to show archive links."""
    if not Post.objects.count(): return []

    # set up vars
    year, month = time.localtime()[:2]
    first = Post.objects.order_by("created")[0]
    fyear = first.created.year
    fmonth = first.created.month
    months = []

    # loop over years and months
    for y in range(year, fyear-1, -1):
		start, end = 12, 0
		if y == year: start = month
		if y == fyear: end = fmonth-1

		for m in range(start, end, -1):
			months.append((y, m, month_name[m]))
    return months

def month(request, year, month):
	posts = Post.objects.filter(created__year=year, created__month=month)
	return render_to_response('blog_list.html', {'posts': posts, 'user': request.user, 'months': mkmonth_lst(), 'archive': True})

def main(request):

	posts = Post.objects.all()
	paginator = Paginator(posts, 3)

	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try: posts = paginator.page(page)
	except (InvalidPage, EmptyPage) :
		posts = paginator.page(paginator.num_pages) 

	return render_to_response('blog_list.html', {'posts': posts, 'user': request.user, 'months': mkmonth_lst()})

