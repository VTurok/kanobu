from django.shortcuts import render
from django.views.generic import View

from .models import News


def posts_list(request):
    news = News.objects.all()
    return render(request, 'posts/posts_lists.html', context={'news': news})
