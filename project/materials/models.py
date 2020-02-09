from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Material(models.Model):
    TYPES = [('news',  'Новость'), ('article', 'Статья')]
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок')
    material_type = models.CharField(max_length=7, choices=TYPES, verbose_name='Тип материала')
    body = models.TextField(blank=True, db_index=True, verbose_name='Текст новости')
    date_create = models.DateTimeField(auto_created=True, verbose_name='Дата создания')
    date_pub = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)