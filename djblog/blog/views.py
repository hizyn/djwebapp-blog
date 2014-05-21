from django.shortcuts import render, render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext

from blog.models import Post, Category

categories = Category.objects.all()

def index(request):
    posts = get_list_or_404(Post)
    return render_to_response('blog/index.html',
        {"posts": posts,
        'categories': categories
        },
        context_instance=RequestContext(request))

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render_to_response('blog/post.html',
        {'post': post,
        'categories': categories
        },
        context_instance=RequestContext(request))


