from django.shortcuts import render
from django.views.generic import View

from .models import News


def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', context={'news': news})
