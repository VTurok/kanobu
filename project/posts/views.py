from django.shortcuts import render
from django.views.generic import View

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', context={'posts': posts})
