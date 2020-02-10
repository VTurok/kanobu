from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .managers import LikeDislikeManager


class LikeDislike(models.Model):
    """
    Класс описывающий модель лайков и дизлайков
    """

    LIKE = 1
    DISLIKE = -1

    VOTES = ((DISLIKE, "Не нравится"), (LIKE, "Нравится"))

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()
