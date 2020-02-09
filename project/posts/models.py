from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок')
    body = models.TextField(blank=True, db_index=True, verbose_name='Текст статьи')
    date_create = models.DateTimeField(auto_created=True, verbose_name='Дата создания')
    date_pub = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)