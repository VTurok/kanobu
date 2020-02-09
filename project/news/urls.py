from django.urls import path, include

urlpatterns = [
    path('', include('news.urls'), name='news_list_url'),
]