from django.conf.urls import url

from . import views
from .models import LikeDislike
from materials.models import Material, Comment

urlpatterns = [
    url(
        r"^article/(?P<pk>\d+)/like/$",
        views.VotesView.as_view(model=Material, vote_type=LikeDislike.LIKE),
        name="article_like",
    ),
    url(
        r"^article/(?P<pk>\d+)/dislike/$",
        views.VotesView.as_view(model=Material, vote_type=LikeDislike.DISLIKE),
        name="article_dislike",
    ),
    url(
        r"^comment/(?P<pk>\d+)/like/$",
        views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE),
        name="comment_like",
    ),
    url(
        r"^comment/(?P<pk>\d+)/dislike/$",
        views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE),
        name="comment_dislike",
    ),
]
