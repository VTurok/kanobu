from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()

from votes.models import LikeDislike


# Create your models here.
class Material(models.Model):
    TYPES = [("Новость", "Новость"), ("Статья", "Статья")]
    title = models.CharField(max_length=150, db_index=True, verbose_name="Заголовок")
    material_type = models.CharField(
        max_length=7, choices=TYPES, verbose_name="Тип материала"
    )
    body = models.TextField(blank=True, db_index=True, verbose_name="Текст новости")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_pub = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    author = models.CharField(max_length=20, db_index=True, verbose_name="Автор")
    votes = GenericRelation(LikeDislike, related_query_name="материалы")

    def get_absolute_url(self):
        return reverse("material_detail_url", kwargs={"pk": self.pk})


class Comment(models.Model):
    material = models.ForeignKey(
        Material, verbose_name="Материал", on_delete=models.CASCADE
    )
    author = models.CharField(max_length=20, db_index=True, verbose_name="Автор")
    body = models.CharField(
        max_length=300, db_index=True, verbose_name="Текст комментария"
    )
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    votes = GenericRelation(LikeDislike, related_query_name="комментарии")
